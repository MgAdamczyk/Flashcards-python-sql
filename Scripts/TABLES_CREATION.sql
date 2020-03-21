CREATE TABLE `progress` (
  `id_progress` INT NOT NULL AUTO_INCREMENT,
  `id_user` INT,
  `id_flashcard` INT,
  `know` BOOLEAN,
  PRIMARY KEY (`id_progress`),
  KEY FK (id_user, id_flashcard)
);

CREATE TABLE `flashcards` (
  `id_flashcard` INT NOT NULL AUTO_INCREMENT,
  `pol` VARCHAR(50),
  `eng` VARCHAR(50),
  `lesson` INT,
  PRIMARY KEY (`id_flashcard`)
);

CREATE TABLE `users` (
  `id_user` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50),
  `password` VARCHAR(50),
  PRIMARY KEY (`id_user`)
);

SHOW TABLES;