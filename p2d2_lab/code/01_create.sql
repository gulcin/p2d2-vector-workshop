CREATE SCHEMA p2d2;

CREATE TABLE p2d2.pictures (
    id          BIGSERIAL   PRIMARY KEY
  , filename    text        NOT NULL
  , embedding   vector(768) NOT NULL
);

ALTER TABLE p2d2.pictures ALTER COLUMN embedding SET STORAGE PLAIN;
