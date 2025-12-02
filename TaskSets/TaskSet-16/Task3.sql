-- List all books borrowed by a specific member (by member_id)
-- Example: list books borrowed by member_id = 1

SELECT
    m.member_id,
    m.first_name,
    m.last_name,
    b.book_id,
    b.title,
    b.author,
    l.loan_id,
    l.loan_date,
    l.due_date,
    l.return_date,
    l.status
FROM Members AS m
JOIN Loans  AS l ON m.member_id = l.member_id
JOIN Books  AS b ON l.book_id   = b.book_id
WHERE m.member_id = 1;  -- change 1 to the specific member_id you want


