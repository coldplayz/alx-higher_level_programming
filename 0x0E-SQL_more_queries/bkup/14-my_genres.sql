-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT tg.name AS name
	FROM tv_shows AS ts
		INNER JOIN tv_show_genres AS tsg
			ON ts.id = tsg.show_id
		INNER JOIN tv_genres AS tg
			ON tsg.genre_id = tg.id
WHERE ts.title = 'Dexter'
ORDER BY name;
