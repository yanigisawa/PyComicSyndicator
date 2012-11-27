CREATE TABLE `ComicRssArchive` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ComicLogId` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_ComicRssArchive_ComicLog` FOREIGN KEY `FK_ComicRssArchive_ComicLog` (`ComicLogId`)
    REFERENCES `ComicLogArchive` (`id`)
)
ENGINE = InnoDB
CHARACTER SET utf8;
