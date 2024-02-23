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
    UNIQUE (email),
    UNIQUE (username)
);

CREATE TABLE article (
    id BIGINT NOT NULL,
    created_by BIGINT NOT NULL,
    title varchar(250)  NOT NULL DEFAULT '',
    body text  NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)
);

CREATE TYPE reaction_type AS ENUM ('favorite');
CREATE TABLE reaction (
    user_id BIGINT NOT NULL,
    article_id BIGINT NOT NULL,
    type reaction_type NOT NULL DEFAULT 'favorite',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (user_id, article_id)

);