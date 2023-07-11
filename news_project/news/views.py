from .models import SearchHistory, SearchResult
import requests
from django.shortcuts import render
from operator import itemgetter
from datetime import datetime
from dateutil import parser


def search_news(request):
    if request.method == 'GET' and 'q' in request.GET:
        keyword = request.GET.get('q')
        refresh = request.GET.get('refresh')
        date_published = request.GET.get('date_published')
        language = request.GET.get('language')

        # Store search history
        search_history = SearchHistory.objects.create(keyword=keyword)

        # Make a request to the News API
        api_key = 'e4ceb64b71e14a19a8586fd594a030c5'
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'

        if date_published:
            # Convert date_published to ISO 8601 format
            published_at = datetime.strptime(date_published, '%Y-%m-%d').date()
            url += f'&from={published_at}'

        response = requests.get(url)
        data = response.json()

        articles = data.get('articles', [])
        

        # Store search results locally
        new_results = []
        for article in articles:
            # source = article.get('source', {}).get('name')
            source_name = article["source"]["name"]
            published_at = article.get('publishedAt')
            parsed_published_at = parser.isoparse(published_at)
            formatted_published_at = parsed_published_at.strftime("%Y-%m-%d %H:%M:%S")
            new_results.append(SearchResult(
                history=search_history,
                title=article.get('title'),
                description=article.get('description'),
                url=article.get('url'),
                published_at=formatted_published_at,
                source_name=source_name,
                source_category=article.get('source', {}).get('category'),
                language=article.get('language'),
                image_url=article.get('urlToImage')
            ))

        SearchResult.objects.bulk_create(new_results)

        if refresh:
            sorted_articles = sorted(articles, key=lambda x: x.get('publishedAt', ''), reverse=True)
        else:
            sorted_articles = sorted(articles, key=lambda x: x.get('publishedAt', ''))

        context = {
            'keyword': keyword,
            'articles': sorted_articles,
        
            
        }

        return render(request, './search_results.html', context)

    return render(request, './search_results.html')


def search_history(request):
    search_history = SearchHistory.objects.all().order_by('-timestamp')
    context = {
        'search_history': search_history
    }
    return render(request, './search_history.html', context)