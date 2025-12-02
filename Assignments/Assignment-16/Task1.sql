-- Schema design for a Library Management System

-- Table: Members
CREATE TABLE Members (
    member_id       INT PRIMARY KEY,
    first_name      VARCHAR(50)  NOT NULL,
    last_name       VARCHAR(50)  NOT NULL,
    email           VARCHAR(100) UNIQUE,
    phone           VARCHAR(20),
    address         VARCHAR(255),
    membership_date DATE         NOT NULL
);

-- Table: Books
CREATE TABLE Books (
    book_id          INT PRIMARY KEY,
    title            VARCHAR(200) NOT NULL,
    author           VARCHAR(100) NOT NULL,
    publisher        VARCHAR(100),
    published_year   INT,
    isbn             VARCHAR(20) UNIQUE,
    category         VARCHAR(50),
    total_copies     INT          NOT NULL,
    available_copies INT          NOT NULL
);

-- Table: Loans
CREATE TABLE Loans (
    loan_id     INT PRIMARY KEY,
    member_id   INT         NOT NULL,
    book_id     INT         NOT NULL,
    loan_date   DATE        NOT NULL,
    due_date    DATE        NOT NULL,
    return_date DATE,
    status      VARCHAR(20) NOT NULL,  -- e.g., 'BORROWED', 'RETURNED', 'OVERDUE'

    CONSTRAINT fk_loans_member
        FOREIGN KEY (member_id) REFERENCES Members(member_id),

    CONSTRAINT fk_loans_book
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
);


