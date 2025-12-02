-- 1) Update a book's availability when it is borrowed
-- Using the existing 'available_copies' column from the Books table in Task1
-- Example: member borrows book_id = 101

UPDATE Books
SET available_copies = available_copies - 1
WHERE book_id = 101
  AND available_copies > 0;  -- prevent negative copies


-- 2) Safely delete a member record
-- We must handle foreign key references from Loans before deleting a member.
-- Example: safely delete member_id = 1
-- First delete all loans associated with the member (if allowed by your rules)
DELETE FROM Loans
WHERE member_id = 1;

-- Now delete the member record
DELETE FROM Members
WHERE member_id = 1;

-- Alternative (soft delete instead of hard delete):
-- Add an 'is_active' BOOLEAN column to Members and then use:
-- UPDATE Members SET is_active = FALSE WHERE member_id = 1;