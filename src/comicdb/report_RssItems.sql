select c.Name, concat(concat('"', cl.ImageUrl), '"'), cl.FetchDate from ComicRss cr
	join ComicLog cl on cr.ComicLogId = cl.Id
	join Comic c on c.Id = cl.ComicId
order by c.Name