from django.shortcuts import render

data_item = {
    'lists': [
        {'name': 'Купить ручку', 'is_done': True},
        {'name': 'Распечатать документы', 'is_done': False},
        {'name': 'Сварить кофе', 'is_done': True},
        {'name': 'Встреча', 'is_done': False, 'date': '01.12.2019'}
    ],
    'user_name': 'Admin',
    'item_name': 'Работа'
}


def item_view(request):
    context = data_item
    return render(request, 'list.html', context)
