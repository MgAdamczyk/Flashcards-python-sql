INSERT INTO users (name, password) VALUES ("Gosia", "gosiasql");
DELETE FROM users WHERE name="Gosia";
SELECT * FROM users;

INSERT INTO flashcards (pol, eng, lesson) VALUES ("kot", "cat", 1);
DELETE FROM flashcards WHERE pol="kot";
SELECT * FROM flashcards;
SELECT pol, eng FROM flashcards WHERE lesson=1;
SELECT lesson, count(*) FROM flashcards GROUP BY lesson;

SELECT * FROM flashcards f LEFT JOIN progress p ON f.id_flashcard = p.id_flashcard WHERE f.lesson = 1 AND (p.id_user = 5 OR p.id_user IS NULL)
UNION
SELECT * FROM flashcards f RIGHT JOIN progress p ON f.id_flashcard = p.id_flashcard WHERE f.lesson = 1 AND (p.id_user = 5 OR p.id_user IS NULL);

INSERT INTO progress (id_user, id_flashcard, know) VALUES (1, 2, false);
DELETE FROM progress WHERE id_flashcard = 2 AND id_user = 1;
SELECT * FROM progress;
UPDATE progress SET know=true WHERE id_flashcard = 2 AND id_user = 1;

TRUNCATE progress;
TRUNCATE users;
TRUNCATE flashcards;