-- =====================================================
-- CUSTOMERS
-- =====================================================

-- =====================================================
-- CUSTOMERS
-- =====================================================

CREATE TABLE IF NOT EXISTS customers (

    customer_id SERIAL PRIMARY KEY,

    customer_name VARCHAR(100) NOT NULL,

    email VARCHAR(150) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    phone VARCHAR(20),

    address TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- =====================================================
-- ADMINS
-- =====================================================

CREATE TABLE IF NOT EXISTS admins (

    admin_id SERIAL PRIMARY KEY,

    admin_name VARCHAR(100) NOT NULL,

    email VARCHAR(150) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- =====================================================
-- QUOTATIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS quotations (

    quotation_id SERIAL PRIMARY KEY,

    customer_id INTEGER REFERENCES customers(customer_id),

    vehicle_type VARCHAR(50),

    brand VARCHAR(100),

    model VARCHAR(100),

    policy_type VARCHAR(50),

    premium_amount NUMERIC(12,2),

    quotation_status VARCHAR(30)
        CHECK (quotation_status IN
        ('Pending','Approved','Rejected','Bought'))
        DEFAULT 'Pending',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- =====================================================
-- POLICIES
-- =====================================================

CREATE TABLE IF NOT EXISTS policies (

    policy_id SERIAL PRIMARY KEY,

    quotation_id INTEGER REFERENCES quotations(quotation_id),

    customer_id INTEGER REFERENCES customers(customer_id),

    policy_number VARCHAR(40) UNIQUE,

    vehicle_type VARCHAR(50),

    policy_type VARCHAR(50),

    premium_amount NUMERIC(12,2),

    start_date DATE,

    expiry_date DATE,

    policy_status VARCHAR(30)
        CHECK (policy_status IN
        ('Active','Expired','Cancelled'))
        DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- =====================================================
-- USER CHAT LOGS
-- =====================================================

CREATE TABLE IF NOT EXISTS user_chat_logs (

    chat_id SERIAL PRIMARY KEY,

    customer_id INTEGER REFERENCES customers(customer_id),

    user_question TEXT,

    ai_answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- =====================================================
-- ADMIN CHAT LOGS
-- =====================================================

CREATE TABLE IF NOT EXISTS admin_chat_logs (

    chat_id SERIAL PRIMARY KEY,

    admin_question TEXT,

    ai_answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


ALTER TABLE customers
ADD COLUMN password VARCHAR(255);

INSERT INTO admins
(admin_name,email,password)
VALUES
(
'Admin',
'admin@acko.com',
'admin123'
);