CREATE INDEX lessons ON flashcards(lesson);
CREATE INDEX updating_flashcard ON progress(id_user, id_flashcard);

DROP INDEX lessons ON flashcards;
DROP INDEX updating_flashcard ON progress;
