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

function openGuest(id)
{
    location.href = "/guest/"+id+"/";
}

function search(query)
{
    //alert(document.getElementById('search-query').value)
    location.href = "https://www.google.com/search?q=site%3Awww.pnsuk.org " + query;
}