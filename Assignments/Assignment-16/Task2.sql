-- Sample INSERT statements for Library Management System

-- Members: 3 sample records (generic / vague values)
INSERT INTO Members (member_id, first_name, last_name, email, phone, address, membership_date) VALUES
(1, 'Member1_First', 'Member1_Last', 'member1@example.com', '9000000001', 'City1, State1', '2023-01-01'),
(2, 'Member2_First', 'Member2_Last', 'member2@example.com', '9000000002', 'City2, State2', '2023-02-01'),
(3, 'Member3_First', 'Member3_Last', 'member3@example.com', '9000000003', 'City3, State3', '2023-03-01');

-- Books: 3 sample records (generic / vague values)
INSERT INTO Books (book_id, title, author, publisher, published_year, isbn, category, total_copies, available_copies) VALUES
(101, 'Sample Book 1', 'Author 1', 'Publisher 1', 2010, 'ISBN-0001', 'Category1', 5, 3),
(102, 'Sample Book 2', 'Author 2', 'Publisher 2', 2015, 'ISBN-0002', 'Category2', 4, 2),
(103, 'Sample Book 3', 'Author 3', 'Publisher 3', 2020, 'ISBN-0003', 'Category3', 3, 3);

-- Loans: 3 sample records (generic / vague values)
INSERT INTO Loans (loan_id, member_id, book_id, loan_date, due_date, return_date, status) VALUES
(1001, 1, 101, '2025-01-01', '2025-01-15', NULL,        'BORROWED'),
(1002, 2, 102, '2025-01-05', '2025-01-20', '2025-01-18','RETURNED'),
(1003, 3, 103, '2025-01-10', '2025-01-25', NULL,        'BORROWED');