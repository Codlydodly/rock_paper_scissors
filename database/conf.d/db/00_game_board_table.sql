CREATE TABLE `game_board`
(
    `id`            int          NOT NULL AUTO_INCREMENT,
    `game_id`       VARCHAR(255) NOT NULL,
    `player_1`      VARCHAR(255) DEFAULT NULL,
    `player_2`      VARCHAR(255) DEFAULT NULL,
    `player_1_move` VARCHAR(10)  DEFAULT NULL,
    `player_2_move` VARCHAR(10)  DEFAULT NULL,
    `game_status`   VARCHAR(30)  DEFAULT NULL,
    `winner`        VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (`id`)
);
