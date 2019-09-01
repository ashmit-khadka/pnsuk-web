function openArticle(id)
{
    location.href = "/article/"+id+"/";
}

function openAdvert(url)
{
    window.open(url);
}

function openProject(id)
{
    location.href = "/project/"+id+"/";
}

function openLink(url)
{
    location.href = url;
}

function openEvent(id)
{
    location.href = "/event/"+id+"/";
}

function search(query)
{
    location.href = "https://www.google.com/search?q=" + query + "+site%3Awww.pnsuk.org";
}