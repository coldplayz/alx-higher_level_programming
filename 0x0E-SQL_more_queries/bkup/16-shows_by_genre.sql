-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

SELECT ts.title AS title, tg.name AS name
	FROM tv_shows AS ts
		LEFT JOIN tv_show_genres AS tsg
			ON ts.id = tsg.show_id
		LEFT JOIN tv_genres AS tg
			ON tsg.genre_id = tg.id
ORDER BY title, name;
