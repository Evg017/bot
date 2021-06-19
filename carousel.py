import json

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        {"photo_id": "Ссылка на изображение","title": "Заголовок карусели","description": "Описание",
        можно также добавить:
        "action": {"type": "open_photo"}, - открывает фотографию карточки
        либо (открывается сслыка при нажатии на карточку): 
        "action": {"type": "open_link", "link": "Ссылка"},
"buttons": [
        {"action": {"type": "open_link", "link": "Ссылка", "label": "Название кнопки"}},
        {"action": {"type": "text", "label": "Название кнопки"}} 
        ]},
        Можно добавить до трёх кнопок. 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

carousel = {"type": "carousel", "elements": [
                    {"photo_id": "-204983322_457239535", "title": "Перезвони мне +79995771202 (2021)", "description": "Седьмой альбом, выпущенный 12 февраля 2021 года (версия без мата!)",
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000459214_11459214_5a5cac0d91359cda7e", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/pmc79995771202", "label": "Ссылка на orcd.co"}}
                        ]},
                
                    {"photo_id": "-204983322_457239535","title": "Перезвони мне +79995771202 (2021)","description": "Седьмой альбом, выпущенный 12 февраля 2021 года (правильная версия)",
             "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000340261_10340261_dd2b05c1b730d1a7e5", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/perezvonimne", "label": "Ссылка на orcd.co"}}
                        ]},
                
                    {"photo_id": "-204940724_457239030", "title": "Я тебя никогда (2018)", "description": "Шестой альбом. Выпущен 11 октября 2018 года",
            "buttons": 
                    [{"action": { "type": "open_link", "link": "https://vk.com/music/album/-2000717298_3717298_8398902188d724ae7d", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/yatebyanikogda", "label": "Ссылка на orcd.co"}}
                        ]},
                
                    {"photo_id": "-204940724_457239031", "title": "Выходи за меня (2017)", "description": "Пятый альбом. Выпущен 24 февраля 2017 года",
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000717482_3717482_5fe17b8e53992b7765", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/vyhodizamenya", "label": "Ссылка на orcd.co"}}
                        ]},
                
                    {"photo_id": "-204940724_457239032", "title": "Байки инсайдера (2015)", "description": "Четвёртый студийный альбом. Выпущен 24 сентября 2015 года",
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000717294_3717294_8c53f326abaf96f803", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/bajkiinsajdera", "label": "Ссылка на orcd.co"}}
                        ]},

                    {"photo_id": "-204940724_457239033", "title": "Без паники (2014)", "description": "Третий студийный альбом. Выпущен 24 сентября 2015 года",
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000341866_5341866_0c00f4027c1c804398", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/bezpaniki", "label": "Ссылка на orcd.co"}}
                        ]},

                    {"photo_id": "-204940724_457239034", "title": "Дети и радуга (2013)", "description": "Второй альбом группы. Выпущен 4 июня 2013 года",
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000736610_3736610_5d2148390b9dc04714", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/detiiraduga", "label": "Ссылка на orcd.co"}}
                        ]},

                    {"photo_id": "-204940724_457239035", "title": "Смачные ништяки (2009)", "description": "Осторожно! САПОЖНИКИ! Осторожно! Выпущен 31 октября 2009 года",
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000717488_3717488_bce16b8c73d039e935", "label": "Перейти к плейлисту в ВК!"}},
                    {"action": {"type": "open_link", "link": "https://orcd.co/smachnyenishtyaki", "label": "Ссылка на orcd.co"}}
                    ]}]}
carousel = json.dumps(carousel, ensure_ascii=False).encode('utf-8')
carousel = str(carousel.decode('utf-8'))

carousel2 = {"type": "carousel", "elements": [
                    {"photo_id": "-204940724_457239036", "title": "Мои дети не будут скучать (2019)", "description": "Второй EP, вышедший 5 декабря 2019 года",
                    "action": {"type": "open_link", "link": "https://orcd.co/moideti"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000242230_6242230_9923e18a9c708fea47", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204940724_457239037","title": "Эволюция (2011)","description": "Первый EP, вышедший в 2011 году",
                    "action": {"type": "open_link", "link": "https://orcd.co/evolyuciya"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/playlist/-2736916_26271196_51f723d79a5e1db8b3", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204983322_457239534", "title": "Фиты и синглы", "description": "Здесь собраны все фиты и синглы!",
                    "action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_25_6a86000f86db49e8a6"},
            "buttons": [
                    {"action": { "type": "open_link", "link": "https://vk.com/music/playlist/440957027_25_6a86000f86db49e8a6", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204940724_457239038", "title": "Неизданное...", "description": "...и не только...",
                    "action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_26_777adab4f844d3bc97"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_26_777adab4f844d3bc97", "label": "Перейти к плейлисту!"}}
                        ]}]}
carousel2 = json.dumps(carousel2, ensure_ascii=False).encode('utf-8')
carousel2 = str(carousel2.decode('utf-8'))

carousel3 = {"type": "carousel", "elements": [
                    {"photo_id": "-204940724_457239039", "title": "Pauzern Carnival (2021)", "description": "Нарезка с Московского карнавала.",
                    "action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_23_e70857c9336644ad41"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_23_e70857c9336644ad41", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204983322_457239533","title": "Anacondaz MTS Live", "description": "Нарезка треков с MTS Live",
                    "action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_12_91e2ead3108a5b68a8"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_12_91e2ead3108a5b68a8", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204940724_457239041", "title": "X Лет", "description": "Нарезка треков с Московсого концерта",
                    "action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_18_1d31f602ec67924ffa"},
            "buttons": [
                    {"action": { "type": "open_link", "link": "https://vk.com/music/playlist/440957027_18_1d31f602ec67924ffa", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204940724_457239042", "title": "Акустика Live", "description": "Запись акустики с концерта",
                    "action": {"type": "open_link", "link": "https://vk.com/music/album/-2000736549_3736549_bd00f238b8112e6ba1"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/album/-2000736549_3736549_bd00f238b8112e6ba1", "label": "Перейти к плейлисту!"}}
                        ]},
                
                    {"photo_id": "-204940724_457239043", "title": "Pauzern Live", "description": "Нарезка с Московского концерта",
                    "action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_17_b9818e81150b911e4d"},
            "buttons": [
                    {"action": {"type": "open_link", "link": "https://vk.com/music/playlist/440957027_17_b9818e81150b911e4d", "label": "Перейти к плейлисту!"}}
                        ]}]}
carousel3 = json.dumps(carousel3, ensure_ascii=False).encode('utf-8')
carousel3 = str(carousel3.decode('utf-8'))

sostav = {"type": "carousel",
            "elements": [
                        {"photo_id": "-204940724_457239049", "title": "Сергей Карамушкин", "description": "Сега - рот группы",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/sega_anacondaz", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/seginaboroda", "label": "Instagram"}},
                        {"action": {"type": "open_link", "link": "https://twitter.com/seginaboroda", "label": "Twitter"}}               
                        ]},

                        {"photo_id": "-204940724_457239050", "title": "Артём Хорев", "description": "Ортём - рот группы",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/ortem_anacondazzz", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/artemkhorev", "label": "Instagram"}},
                        {"action": {"type": "open_link", "link": "https://twitter.com/artemkhorev", "label": "Twitter"}}               
                        ]},

                        {"photo_id": "-204940724_457239051", "title": "Илья Погребняк", "description": "Бешеный пёс, гитара",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/rap_guitar", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/iliapogrebniak", "label": "Instagram"}},
                        {"action": {"type": "open_link", "link": "https://twitter.com/IliaPogrebniak", "label": "Twitter"}}               
                        ]},

                        {"photo_id": "-204940724_457239052", "title": "Евгений Форманенко", "description": "Евгей, главный по басу",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/rap_bass", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/mo4islona", "label": "Instagram"}},
                        {"action": {"type": "open_link", "link": "https://twitter.com/mo4islona", "label": "Twitter"}}               
                        ]},
                        
                        {"photo_id": "-204940724_457239053", "title": "Евгений Стадниченко", "description": "Женя, ударные",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/kickingdasnare", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/kickindasnare", "label": "Instagram"}},
                        {"action": {"type": "text", "label": "Twitter - Утерян"}}               
                        ]},
                        
                        {"photo_id": "-204940724_457239057", "title": "Александр Полежаев", "description": "Звукорежиссер",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/polezhaj", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/polezhaj", "label": "Instagram"}},
                        {"action": {"type": "open_link", "link": "https://twitter.com/Polezhaj", "label": "Twitter"}}              
                        ]},

                        {"photo_id": "-204940724_457239056", "title": "Валентин Бойков", "description": "Валя, ты же менеджер, а где у нас лимон и джем?",
                        "action": {"type": "open_photo"},
            "buttons": [
                        {"action": {"type": "open_link", "link": "https://vk.com/id3033976", "label": "Профиль в VK"}},
                        {"action": {"type": "open_link", "link": "https://www.instagram.com/valkov", "label": "Instagram"}},
                        {"action": {"type": "text", "label": "Twitter - Не найден"}}              
                        ]}]}
sostav = json.dumps(sostav, ensure_ascii=False).encode('utf-8')
sostav = str(sostav.decode('utf-8'))
