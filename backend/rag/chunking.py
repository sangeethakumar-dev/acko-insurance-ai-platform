import re
from langchain_text_splitters import RecursiveCharacterTextSplitter


#FAQ Chunking
# The FAQ PDF uses Q / A format. We find each Q line and extract
# the text up to the next Q line as one chunk.
# This is the same pattern as chunk_qa_pairs() in train_faq.py

def faq_chunking(raw_text):
    # Remove header/footer noise that repeats across pages
    _NOISE = re.compile(
        r'(acko Frequently Asked Questions|AI-Generated Content|acko\.com|'
        r'Page \d+|Motor \| Health \| Claims|Supplementary Sections|'
        r'Insurance Reference Guide)',
        re.IGNORECASE
    )

    def clean_text(text):
        lines = [l for l in text.splitlines() if not _NOISE.search(l)]
        return '\n'.join(lines)


    # The Q lines in the PDF start with "Q " followed by a question word
    _Q_PATTERN = re.compile(
    r'(?m)^Q\s+(?:[A-Z][0-9]+\.\s+|'
    r'(?:What|How|Is|Are|Can|Does|Do|My|I |Should|Why|When|Who|'
    r'Which|Will|Where|Was|Has|Have|If))'
    )

    _SECTION_PATTERN = re.compile(r'SECTION\s+[A-Z]\s*[--]\s*(.+?)(?:\n|$)', re.IGNORECASE)

    text = clean_text(raw_text)
    positions = [m.start() for m in _Q_PATTERN.finditer(text)]
    print(f'Q&A pairs found: {len(positions)}')

    chunks = []
        
    for idx, start in enumerate(positions):
        end   = positions[idx + 1] if idx + 1 < len(positions) else len(text)
        block = text[start:end].strip()
        lines = block.splitlines()

        q_lines, a_lines, in_answer = [], [], False
        for line in lines:
            s = line.strip()
            if not s:
                continue
            if not in_answer and re.match(r'^A\s+', s):
                in_answer = True
                a_lines.append(re.sub(r'^A\s+', '', s))
            elif in_answer:
                a_lines.append(s)
            else:
                q_lines.append(re.sub(r'^Q\s+', '', s))

        question = ' '.join(q_lines).strip()
        answer   = ' '.join(a_lines).strip()
        if not question or not answer or len(answer) < 30:
            continue

        #Find the nearest section header
        section = 'General'
        for m in _SECTION_PATTERN.finditer(text[:start]):
            section = m.group(1).strip()

        # Format exactly as train_faq.py formats it
        doc_text = (
            f'SECTION: {section}\n'
            f'QUESTION: {question}\n'
            f'ANSWER: {answer}'
            )
        chunks.append({
            "id": f"faq_{idx+1:04d}",
            "text": doc_text,
            "metadata": {
            "pdf_name": "faq",
            "chunk_type": "faq",
            "section": section,
            "question": question
            }
        })

    return chunks


#Motor Policy and Health Policy Chunking

def policy_chunking(raw_text, pdf_name="policy"):
    subchapter_pattern = re.compile(
    r'(?m)^(\d+\.\d+)\s*(.+)$'
)
    matches = list(subchapter_pattern.finditer(raw_text))

    if not matches:
        print("No subchapter patterns found!")
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    final_chunks = []

    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx+1].start() if idx+1 < len(matches) else len(raw_text)

        section_text = raw_text[start:end].strip()

        section_number = match.group(1)
        section_title = match.group(2).strip()

        if len(section_text) <= 1000:
            final_chunks.append({
                "id": f"policy_{idx+1}",
                "text": section_text,
                "metadata": {
                    "pdf_name": pdf_name,
                    "chunk_type": "policy",
                    "section_number": section_number,
                    "section_title": section_title
                }
            })

        else:
            split_chunks = splitter.split_text(section_text)

            for sub_idx, chunk in enumerate(split_chunks):
                final_chunks.append({
                    "id": f"policy_{idx+1}_{sub_idx+1}",
                    "text": chunk,
                    "metadata": {
                        "pdf_name": pdf_name,
                        "chunk_type": "policy",
                        "section_number": section_number,
                        "section_title": section_title
                    }
                })

    return final_chunks
