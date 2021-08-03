DROP TRIGGER IF EXISTS `applyNewDataUpdate`

DELIMITER //
CREATE TRIGGER `applyNewDataUpdate`
AFTER INSERT ON gamedata_gamesubmissions
FOR EACH ROW
BEGIN 
	IF NEW.game_id IN (SELECT gg.id FROM gamedata_gameinfo gg)
	THEN 
		CALL ps_average_no_outlier(NEW.game_id, @diff, @times, @count);
		UPDATE gamedata_gameinfo gg
		SET gg.difficulty = @diff, gg.time = @times, gg.counts = @count
		WHERE NEW.game_id = gg.id;
	END IF;
END //

DELIMITER ;
