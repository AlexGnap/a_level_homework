DROP TABLE IF EXISTS movie_people;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS genre;

--create genre table
CREATE TABLE genre (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);


-- create table movie
CREATE TABLE movie (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    tagline VARCHAR(255),
    summary TEXT,
    release_year INT,
    genre_id INT REFERENCES genre(id)
);


--create table people
CREATE TABLE people(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_day DATE

);


CREATE TABLE movie_people (
    movie_id INT REFERENCES movie(id),
    people_id INT REFERENCES people(id),
    character_name VARCHAR(255),
    is_director BOOLEAN DEFAULT FALSE,
    is_writer BOOLEAN DEFAULT FALSE,
    PRIMARY KEY(movie_id, people_id)
);


INSERT INTO genre(name)
VALUES
('Comedy'),
('Drama'),
('Horror'),
('Adventure'),
('Action');


INSERT INTO movie(title, tagline, summary, release_year, genre_id)
VALUES
('Equalizer', 'What do you see when you look at me?','A man who believes he has put his mysterious past behind him cannot stand idly by when he meets a young girl under the control of ultra-violent Russian gangsters.',2015, 5),
('Training day', 'The only thing more dangerous than the line being crossed, is the cop who will cross it', 'A rookie cop spends his first day as a Los Angeles narcotics officer with a rogue detective who isn`t what he appears to be.', 2001, 5),
('American Gangster ', 'There are two sides to the American dream.', 'An outcast New York City cop is charged with bringing down Harlem drug lord Frank Lucas, whose real life inspired this partly biographical film.', 2007, 2),
('Antwone Fisher', 'Inspired by a true story.', 'Antwone Fisher, a young navy man, is forced to see a psychiatrist after a violent outburst against a fellow crewman. During the course of treatment a painful past is revealed and a new hope begins.', 2007, 2),
('Doctor Dolitle', 'He does`t just talk to the animals!', 'A doctor discovers that he can communicate with animals.', 1998, 1),
('Indiana Jones and the Dial of Destiny', 'A legend will face his destiny.', 'Archaeologist Indiana Jones races against time to retrieve a legendary artifact that can change the course of history.', 2023, 4);


INSERT INTO people (name, birth_day)
VALUES
('Denzel Washington', '1963-01-01'),
('Eddie Murphy', '1957-02-02'),
('Harrison Ford', '1958-05-28'),
('Antonio Banderas', '1954-03-07'),
('Oliver Platt', '1950-06-01'),
('Sung Kang', '1963-02-09');


INSERT INTO movie_people (movie_id, people_id, character_name, is_director, is_writer)
VALUES
(1, 1, 'Robert McCall', FALSE, FALSE),
(2, 1, 'Alonzo', FALSE, FALSE),
(6, 4, 'Renaldo', FALSE, FALSE),
(3, 1, 'Frank Lucas', FALSE, FALSE),
(3, 6, 'Cop', FALSE, FALSE),
(4, 1, 'Antwone Fisher', FALSE, FALSE),
(5, 2, 'Dr. Dolittle', TRUE, FALSE),
(5, 5, 'Dr. Mark Weller', FALSE, FALSE),
(6, 3, 'Indiana Jones', FALSE, FALSE);
