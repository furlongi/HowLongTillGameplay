DROP PROCEDURE IF EXISTS `ps_average_no_outlier`;

DELIMITER //

CREATE PROCEDURE `ps_average_no_outlier`(IN id INT, OUT diff DOUBLE, OUT times DOUBLE, OUT count INT)
BEGIN
	WITH dist AS (SELECT AVG(gs.difficulty) AS avgD, AVG(gs.time) AS avgT, 
					   STDDEV(gs.difficulty) AS stdevD, STDDEV(gs.time) AS stdevT,
					   COUNT(*) AS num
				FROM gamedata_gamesubmissions gs
				WHERE gs.game_id = id)
	
	SELECT d.diff AS `difficulty`, t.times AS `times`, d.count AS `count`
	INTO diff, times, count
	FROM (
		SELECT AVG(gg.difficulty) AS diff, dist.num AS count
		FROM gamedata_gamesubmissions gg
		INNER JOIN dist
			ON gg.difficulty BETWEEN dist.avgD-(1.5*dist.stdevD) AND dist.avgD+(1.5*dist.stdevD)
		) AS d
	JOIN (
		SELECT AVG(gg.time) AS times
		FROM gamedata_gamesubmissions gg
		INNER JOIN dist
			ON gg.time BETWEEN dist.avgT-(1.5*dist.stdevT) AND dist.avgT+(1.5*dist.stdevT)
		) AS t;			
END //
DELIMITER ;


