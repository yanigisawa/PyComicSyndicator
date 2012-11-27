CREATE TABLE `ComicLogArchive` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ComicId` INT NOT NULL,
  `FetchDate` DATETIME NOT NULL,
  `ImageUrl` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX IX_ComicLogArchive_FetchDate(`FetchDate`),
  CONSTRAINT `FK_ComicLogArchive_ComicId` FOREIGN KEY `FK_ComicLogArchive_ComicId` (`ComicId`)
    REFERENCES `Comic` (`Id`)
)
ENGINE = InnoDB
CHARACTER SET utf8;
