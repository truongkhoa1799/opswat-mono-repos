DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS article;

CREATE TABLE user (
    id BIGINT NOT NULL,
    email varchar(255)  NOT NULL DEFAULT '',
    username varchar(255)  NOT NULL DEFAULT '',
    fullname VARCHAR(255)  DEFAULT '',
    hashed_password varchar(255)  NOT NULL DEFAULT '',
    salt varchar(255)  NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    UNIQUE (email, username)
);

CREATE TABLE article (
    id BIGINT NOT NULL,
    title varchar(250)  NOT NULL DEFAULT '',
    body text  NOT NULL DEFAULT '',
    favourite_count INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);
