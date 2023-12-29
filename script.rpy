﻿# Определение персонажей игры.
define Anna = Character('Анна', color ="#c97c9a", image = "anna")
define Elio = Character('Элио', color = "#884924", image = "elio")
define Elio2 = Character('...', color = "#884924", image = "elio")
define Margo = Character('Марго', color ="#9c2f8a", image = "margo")
define girl = Character('Девушка', color ="#9c2f8a", image = "margo")
define Raphael = Character('Рафаэль', color ="#435db4", image = 'raphael')
define Raphael2 = Character('...', color ="#435db4", image = 'raphael')
define teacher = Character('Преподаватель', color ="#1c884c", image = 'teacher')

#музыка и звуки
define audio.musnormal = "music/normal music.mp3"
define audio.musintense = "music/intense music.mp3"
define audio.city = "sounds/city.mp3"
define audio.scream = "sounds/Anna's scream.mp3"
define audio.door = "sounds/door.mp3"
define audio.fountain = "sounds/fountain.mp3"
define audio.guitar = "sounds/guitar.mp3"
define audio.moving = "sounds/moving.mp3"
define audio.portal = "sounds/portal.mp3"
define audio.rustleOfLeaves = "sounds/rustle of leaves.mp3"
define audio.talk = "sounds/talk.mp3"
define audio.wardrobe = "sounds/wardrobe.mp3"
define audio.running = "sounds/running.mp3"

init:
    $ left2 = Position(xalign = 0.2, yalign = 0.6)
    $ right2 = Position(xalign = 0.8, yalign = 0.4)
    $ center2 = Position(yalign = 0.6)
    $ left3 = Position(xalign = 0.0, yalign = 0.4)
    $ center3 = Position(xalign = 0.5, yalign = 0.1)
    $ right3 = Position(xalign = 1.0, yalign = 0.4)

# Игра начинается здесь:
label start:
    scene bg first meet
    play music musnormal
    $ renpy.notify("XIX век")
    "Анна прогуливалась по саду, любовалась красивыми пейзажами и блуждала по тропинкам."
    show anna normal at left2
    Anna "«До чего же тут красиво.. какие прекрасные цветы.. как они вкусно пахнут..»"
    play sound rustleOfLeaves
    stop music fadeout 1
    play music musintense
    Anna "«А?! Что это за звуки?»"
    show anna fright at center2

    menu:
        "Что делать?"
        "Убежать":
            jump escape
        "Закричать":
            jump scream
    return


label escape:
    scene bg first meet
    with fade
    play sound running
    "Анна пытается убежать, но незнакомец оказывается быстрее неё и догоняет её"
    show elio normal at right2
    show anna fright at left2
    Elio2 "Извини, что напугал тебя, я не хотел."
    Anna normal "Кто ты такой?! И что ты забыл в нашем саду?"
    Elio "Меня зовут Элио, я приехал из другого имения, чтобы передать телеграмму твоему отцу, на обратном пути я заблудился, можешь помочь найти выход?"
    stop music fadeout 1
    play music musnormal
    Anna "Ну.. так уж и быть, пойдём."
    call continuation from _call_continuation
    return

label scream:
    scene bg first meet
    with fade
    play sound scream
    "Анна изо всех сил крикнула, чтобы привлечь внимание окружающих."
    show anna scream at left2
    show elio normal at right2
    Anna "Кто ты такой?! Я сейчас на тебя собак спущу!"
    Elio2 "Тшш, извини, что напугал тебя, я не хотел."
    Anna normal "Что ты забыл в нашем саду?"
    Elio "Меня зовут Элио, я приехал из другого имения, чтобы передать телеграмму твоему отцу, на обратном пути я заблудился, можешь помочь найти выход?"
    stop music fadeout 1
    play music musnormal
    Anna "Ну.. так уж и быть, пойдём."
    call continuation from _call_continuation_1
    return

label continuation:
    scene bg garden
    with fade
    play sound fountain
    show anna normal at left2
    show elio normal at right2
    Elio "Спасибо, что помогла, но я всё еще не знаю имени своей спасительницы."
    Anna "Ой, прости, забыла представиться, меня зовут Анна."
    Elio "Приятно познакомиться, но мне уже пора уходить."
    Anna "Очень жаль, но, я надеюсь, что мы когда-нибудь ещё увидимся…"
    Elio "Может быть и встретимся, кто его знает. Однако обидно, что сейчас не могу провести больше времени с такой замечательной девушкой."
    scene bg garden
    show anna embarrassment at center2
    Anna "..."
    Anna normal "«Какой интересный молодой человек, что за рисунок у него был на шее? Я раньше не видела такого, нужно за ним проследить» "
    scene bg road
    with fade
    "Элио шёл по тропинке и резко свернул в лес."
    show anna normal at center2
    Anna "«Куда он свернул?»"
    scene bg forest
    "Элио остановился среди деревьев, закатал рукав пиджака и вызвал портал с помощью прибора, встроенного ему в руку."
    play sound portal
    scene  bg portal
    show anna normal at center2
    Anna "«Что это такое? Он что колдун?»"
    hide anna
    "Элио запускает портал и перемещается. После того как Элио исчез, Анне стало интересно, что это за необычное явление, поэтому она подошла к порталу. "

    menu:
        "Что делать?"
        "Пойти за Элио":
            jump goAfterElio
        "Остаться":
            jump stay
    return



label goAfterElio:
    "Анна шагает сама в портал и перемещается."
    play sound moving
    call chapter2 from _call_chapter2
    return

label stay:
    "Анна детально рассматривает портал и пытается понять, что это такое, тут неожиданно портал снова начинает работать и перемещает Анну."
    play sound moving
    call chapter2 from _call_chapter2_1
    return

label chapter2:
    scene bg library with fade
    show anna normal
    $ renpy.notify("Настоящее время")
    Anna "«Что, что произошло? Где я?»"
    hide anna
    play sound talk
    "Анна, ошарашенная и испуганная, оглядела библиотеку в поисках ответов на свои вопросы. Она не могла понять, как оказалась здесь. Вдруг её размышления прервала студентка первого курса, которая пристально всматривалась в неё."
    show margo normal at right2
    show anna normal at left2
    girl "Ты в порядке? Ты выглядишь так, будто увидела призрака."
    Anna "Ты видела то, что со мной произошло?"
    girl "Ну, что именно ты имеешь в виду?"
    Anna "Я не знаю, как я сюда попала... "
    girl "Расскажи последнее что с тобой происходило?"
    Anna "Я... Я действительно не знаю, как я попала сюда... Я была в лесу... Потом какая-то странная вспышка и вот я здесь."
    girl "Так, мне кажется, тебе нужно выйти на воздух, пойдём."
    play sound city

    scene bg city1
    "Как только они вышли из библиотеки, Анна оказалась в полном шоке. Она впервые увидела окружающий мир: люди, автомобили, высокие здания."
    "Все это было так необычно и непонятно для нее. Анна оглядывалась по сторонам, уставившись на неоновые вывески и быстро движущиеся машины."
    show anna normal at left2
    show margo normal at right2
    Anna "Что это за место? Что это за странные шумы и запахи? А почему все куда-то спешат? Всё такое... странное."
    girl "Что тебя удивляет? Это всего лишь город."
    Anna "Я никогда раньше не видела этого."
    girl "Стоп, ты правда хочешь сказать, что каким-то образом переместилась сюда? И всё что ты говорила в библиотеке правда?"
    Anna "Да, только я не понимаю, как это произошло."
    girl "Расскажи о себе, откуда ты? Насколько я помню, такие платья носили в 19 веке?"
    Anna "Да, ты права, такие платья носят в 19 веке. Меня зовут Анна, я живу в небольшом городке, в своём поместье и у нас нет таких высоких зданий как у вас."
    girl "Невероятно! Ты действительно из 19 века? Я просто не могу поверить в это. Давай пойдем ко мне домой, там мы сможем поговорить и разобраться во всем. Я не могу оставить тебя здесь на улице, особенно если ты действительно из другой эпохи."
    hide anna
    hide margo
    "Когда они шли по улице, Анна неустанно задавала вопросы о всем и везде. Она останавливала Марго каждые несколько шагов, чтобы уточнить, что это за место и как все это работает."
    "После множества вопросов они, наконец, добрались до дома. Анна все еще внимательно рассматривала мебель и украшения, недоумевая от каждой детали."
    scene bg room margo
    show margo normal at right2
    show anna normal at left2
    girl "Проходи в комнату."
    Margo "Кстати, забыла представиться, я Марго."
    Anna "Приятно познакомиться."
    Margo "Взаимно."
    Anna "У тебя здесь так много странных вещей... Что это за громадные книжки?"
    Margo smile "Это все мои учебные материалы по UX/UI-дизайну. Я учусь делать веб-сайты и приложения удобными для использования."
    Anna "Веб-сайты? Приложения? Что это такое?"
    Margo "Ну, веб-сайты - это как книги, которые можно прочитать на экране компьютера, а приложения - это как игрушки, которые можно запустить на телефоне или планшете."
    Anna "Я никогда не использовала компьютер или телефон. Что такое интерфейс?"
    Margo "Интерфейс - это как дверь в дом. Чем она удобнее и красивее, тем приятнее заходить внутрь."
    Anna "Теперь всё стало гораздо понятнее. Спасибо, Марго, что так легко объяснила!"
    Margo normal "Давай продолжим нашу беседу во время прогулки, заодно продолжу знакомить тебя с городом."
    Anna "С удовольствием!"
    Margo "Но для начала тебя нужно переодеть, чтобы ты выглядела как обычная современная девушка."
    Anna "Ну.. хорошо, но у меня нет другой одежды."
    Margo "Я сейчас что-нибудь поищу для тебя."
    play sound wardrobe
    Margo "Вот держи."
    Anna "Вау, оно прекрасно."
    Margo smile "Тебе очень идёт, теперь мы готовы отправляться в путь."
    hide anna
    hide margo
    play sound guitar
    "Выходя из комнаты, Анна услышала звуки гитары, которые доносились из другой комнаты."
    show anna normal at left2
    show margo normal at right2
    Anna "Кто это играет?"
    Margo "Оо это мой братец, пойдём покажу."
    play sound door
    scene bg raphael with fade
    "..."
    scene bg room raphael with fade
    show margo normal at left3
    show anna normal at center3
    show raphael normal at right3
    Anna "Хорошо играешь."
    Raphael2 "Спасибо большое."
    Anna "..."
    Raphael2 "..."
    Raphael2 "Марго, может познакомишь?"
    Margo "Ой, да, точно. Анна, это Рафаэль, Рафаэль, это Анна."
    Raphael smile "Приятно познакомиться, Анна."
    Anna "Взаимно."
    Raphael "Ты выглядишь просто очаровательно."
    Anna embarrassment "Спасибо."
    Margo "Та-ак, что-то мы задержались, нам пора."
    Raphael smile "Буду ждать встречи с тобой, Анна."
    Anna "..."

    scene bg city2
    play sound city
    "Марго показывает Анне разные интересные места, рассказывает о своих любимых кафе, уютных переулках и старинных зданиях."
    show anna normal at left2
    show margo normal at right2
    Margo "Слушай, мы сейчас как раз находимся недалеко от большого торгового комплекса, пойдём поищем тебе одежду?"
    Anna "Да, можно. Не буду же я постоянно брать твои вещи."
    hide anna
    hide margo
    "Марго повела Анну по своим любимым магазинам."
    scene bg timeskip
    "..."
    show anna normal at left2
    show margo normal at right2
    Margo "Как тебе твои новые образы?"
    Anna "Они просто потрясающие."
    Margo "Я рада, что тебе понравилось, правда, мы что-то задержались, нам уже пора домой, так как мне еще нужно успеть сделать домашнее задание."
    Anna "Тогда пойдём скорее."
    hide anna
    hide margo
    "По пути домой Анна неожиданно замечает в толпе людей знакомое лицо."
    show anna normal at left2
    show margo normal at right2
    Anna "«Это был Элио!»"
    stop music fadeout 1
    play music musintense
    Anna "Стой, подожди секунду."
    Margo "Что случилось?"
    Anna "Мне кажется, что я увидела своего знакомого. Я сейчас.."
    hide margo normal
    Anna "Элио!"
    show elio normal at right2
    Elio "А?!"
    Anna "Здравствуй, у меня к тебе есть парочка вопросов."
    Elio "Извините, вы меня с кем-то путаете, меня зовут Кирилл. И мне уже пора уходить."
    Anna "Нет, стой, это точно ты! Почему ты делаешь вид, что не знаешь меня?"
    Elio "Нет, Вы что-то путаете. До свидания!"
    hide anna
    hide elio
    "Не успела Анна и оглянуться, как Элио исчез в толпе."
    call chapter3 from _call_chapter3
    return

label chapter3:
    scene bg room margo
    play music musnormal
    $ renpy.notify("Тем же вечером")
    "Марго сидит за рабочим столом и делает домашнее задание."
    show anna normal at left2
    show margo normal at right2
    Anna "Выглядит прикольно, я бы тоже хотела так уметь делать."
    Margo "Если тебе интересно, то я могу как-нибудь взять тебя с собой в университет."
    Anna "Да, конечно, обязательно бери."
    Anna "А сейчас, чтобы тебя не отвлекать, я пойду осмотрю дом, как вы тут живёте."
    Margo "Слушай, закинь тогда вещи в стирку, пожалуйста."
    Anna "«В стирку» это как?"
    Margo "Есть стиральная машина, в которую закидываешь вещи, запускаешь машинку, и она сама всё стирает."
    Anna "Ого, у нас стирают всё вручную, но хорошо, я попробую. А куда мне нужно идти?"
    Margo "Как выйдешь из комнаты, поверни направо, затем иди прямо, и по левую сторону от тебя будет дверь, за которой находится стиральная машина."
    Anna "Надеюсь, я всё запомнила."
    call whereToGo from _call_whereToGo
    return

label whereToGo:
    scene bg flat
    show anna normal
    Anna "Так, куда мне Марго сказала идти?"
    menu:
        "Куда?"
        "Налево":
            jump toLeft
        "Направо":
            jump toRight
        "Прямо":
            jump straight
    return

label toLeft:
    scene bg kitchen
    "Анна повернула налево, но она пришла в кухню."
    show anna normal
    Anna "Нет, кажется, я не туда пришла."
    call whereToGo from _call_whereToGo_1
    return

label toRight:
    scene bg hallway
    "Анна повернула направо и попала в коридор."
    show anna normal
    Anna "Мне кажется, я на верном пути."
    call whereToGo2 from _call_whereToGo2
    return

label whereToGo2:
    scene bg hallway
    show anna normal
    menu:
        "Куда?"
        "Прямо":
            jump straight2
        "Направо":
            jump toRight2
        "Налево":
            jump toLeft2
    return

label straight2:
    scene bg hallway
    "В конце коридора Анна увидела дверь по левую сторону."
    show anna normal
    Anna "Вроде вот та дверь, о которой говорила Марго."
    scene bg washing machine
    "Анна открывает дверь и видит там стиральную машинку."
    show anna normal at left2
    Anna "Так, теперь надо понять, как ей пользоваться.."
    show raphael smile at right2
    Raphael "Думаю, тебе необходима помощь."
    Anna "Если тебе не трудно, то можешь объяснить, как это работает?"
    Raphael normal "Всё просто, закидываешь вещи в барабан, выбираешь нужный режим и готово."
    Anna "Так странно, что вы сами стираете вещи, у нас этим занимается прислуга."
    Raphael "Что значит у вас? Ты разве не учишься вместе с Марго в университете?"
    Anna "Нет, я оказалась в вашем мире случайно."
    Raphael "Как это? Пойдём ко мне в комнату - объяснишь."
    Anna "Хорошо."
    hide anna
    hide raphael
    "По дороге в комнату Анна рассказала вкратце всю суть происходящего."
    scene bg room raphael
    show anna normal at left2
    show raphael normal at right2
    Raphael "Удивительно, я думал, что такое бывает только в сказках."
    Anna "Как видишь, бывает и наяву."
    Raphael "Расскажи ещё что-нибудь, о своей семье, например."
    Anna "Семья.. как же я скучаю по отцу, матери."
    Raphael "Я понимаю, это нелегко быть вдали от своих близких."
    Anna "Я так соскучилась по дому, по привычным местам."
    Raphael "Тебе важна поддержка семьи и близких людей. Я могу понять, как это одиноко быть вдали от родных. Но будь уверена, здесь ты не одна. У тебя есть я, Марго, и мы будем рядом с тобой, чтобы поддержать и помочь."
    Anna "Спасибо тебе, Рафаэль."
    Raphael "Уже поздно, может пойдём спать?"
    Anna "Да, пора уже. Спокойной ночи."
    Raphael smile "Спокойной ночи."
    call chapter3Cont from _call_chapter3Cont
    return

label toRight2:
    scene bg flat
    show anna normal
    Anna "Вроде это та дверь, о которой говорила Марго."
    hide anna
    "Анна открывает дверь, но вместо стиральной машины видит там Рафаэля."
    scene bg room raphael
    show anna normal at left2
    show raphael normal at right2
    Raphael "?"
    Anna "Ой, извини, я перепутала дверь."
    call whereToGo2 from _call_whereToGo2_1
    return

label toLeft2:
    scene bg dressing room
    "Анна попала в комнату с огромным количеством одежды, что напоминало гардероб."
    show anna normal
    Anna "Вау, как здесь много разной одежды."
    Anna "Но это совсем не то место, в которое я должна была прийти."
    call whereToGo2 from _call_whereToGo2_2
    return

label straight:
    show anna normal
    Anna "Ой, там же нет прохода. Кажется, я неправильно запомнила."
    call whereToGo from _call_whereToGo_2
    return

label chapter3Cont:
    scene bg room margo
    $ renpy.notify("На следующее утро")
    show anna normal at left2
    show margo normal at right2
    Margo "Эй, просыпайся, погнали в магазин, у нас нет еды."
    Anna "Встаю, встаю."
    hide anna
    hide margo
    "Анна еле как встала, ведь она не привыкла так рано просыпаться. Вместе с Марго они пришли в магазин."

    scene bg shop
    "Анну удивляют продукты и товары, которые продаются в магазине, а также сам процесс покупки."
    show anna normal at left2
    show margo normal at right2
    Anna "Марго, я просто не могу поверить, как много всего есть в этом магазине! Смотри, сколько продуктов разных!"
    Margo smile "Да, современные магазины впечатляют. Здесь можно найти практически все, что нужно для жизни."
    scene bg timeskip
    "..."
    scene bg street
    play sound city
    "Когда они вышли из магазина, Анна поняла, что пакеты гораздо тяжелее, чем она ожидала. Она незамедлительно поняла, что никогда не могла бы донести все это до дома самостоятельно. В этот момент она заметила Рафаэля, который случайно проходил мимо."
    show anna normal at left2
    show margo normal at right2
    Anna "О боже, насколько тяжёлые эти пакеты! Я не могу поверить, как много мы купили."
    Margo "Да, они действительно огромные. Даже не представляю, как мы с ними до дома дойдем."
    hide anna
    hide margo
    show margo normal at left3
    show anna normal at center3
    show raphael normal at right3
    Raphael "Привет, девочки! Рад видеть вас. Что-то вижу, что вам тяжело нести эти пакеты, давайте я помогу."
    Margo smile "Раф, спасибо! У меня уже руки болят от этих пакетов."
    Anna "Действительно, спасибо, Рафаэль! Очень приятно, что ты так заботлив."

    scene bg flat
    show margo normal at left3
    show anna normal at center3
    show raphael normal at right3
    Raphael "Вот мы и дошли наконец."
    Anna "Еще раз спасибо, Рафаэль. Я не знаю, что бы мы делали без твоей помощи."
    Raphael "Не стоит благодарности, Анна. Я всегда рад помочь."
    Raphael "Кстати, я написал новую песню. Не хотела ли бы ты её послушать?"
    menu:
        "Согласиться":
            jump agree
        "Отказаться":
            jump refuse
    return

label agree:
    scene bg flat
    show anna normal at left2
    show raphael normal at right2
    Anna "Конечно, я с радостью послушаю твою новую композицию."
    Raphael "Пойдём тогда в комнату."

    scene bg room raphael
    play sound guitar
    "Рафаэль начинает играть на гитаре. Его аккорды заполняют комнату, создавая гармоничную мелодию. В то время, как он играет, Анна восхищенно слушает. "
    show anna normal at left2
    show raphael normal at right2
    Anna "Вау, Рафаэль, эта песня просто потрясающая! Ты очень талантливый музыкант."
    Raphael smile "Спасибо, Анна. Я очень рад, что она тебе понравилась."
    Raphael normal "Кстати, расскажи о своих увлечениях."
    Anna "Я люблю рисовать, поэтому раз в неделю я любила засиживаться в саду, чтобы запечатлить красоту природы на листке бумаги."
    Raphael "Потрясающе, хотел бы я взглянуть на твои работы."
    Anna "Может быть, я нарисую что-нибудь и здесь."
    Raphael smile "..."
    Anna "..."
    Raphael normal "Я бы с радостью посидел с тобой ещё, но мне уже пора, у меня пара."
    Anna normal "Конечно, конечно, иди."
    hide anna
    hide raphael
    "Анна вернулась к себе в кровать и погрузилась в глубокий сон."
    call university from _call_university
    return

label refuse:
    scene bg flat
    show anna normal at left2
    show raphael normal at right2
    Anna "Нет, спасибо, Рафаэль. Мне уже пора спать."
    Raphael "Ну хорошо, в следующий раз тогда."
    hide anna
    hide raphael
    "Анна уходит в свою комнату, где начинает думать об Элио. Она задается вопросом, куда он пропал и почему не узнал её. С этими раздумьями она погрузилась в глубокий сон."
    call university from _call_university_1
    return

label university:
    scene bg lecture hall
    $ renpy.notify("Спустя две недели")
    show teacher
    teacher "Здравствуйте, уважаемые студенты. Сегодня мы говорим с вами об UX/UI-дизайнере. Начнём с того, кто такой UX/UI – дизайнер."
    teacher "Кратко говоря UX ― это функционал интерфейса, UI ― его внешний вид."
    teacher "Разница между UX и UI в том, что UX дизайнер планирует то, как вы будете взаимодействовать с интерфейсом и какие шаги вам нужно предпринять, чтобы сделать что-то. А UI дизайнер придумывает, как каждый из этих шагов будет выглядеть."
    teacher "UX и UI так тесно связаны, что иногда грань между понятиями смывается. Поэтому и UX, и UI обычно занимается один дизайнер и его профессия пишется через /."
    call lecture from _call_lecture
    return

label lecture:
    scene bg lecture hall
    $ q = []
    while len(q) < 3:
        menu:
            "Чем занимается UI/UX - дизайнер?" if not 1 in q:
                $ q.append(1)
                show teacher
                teacher "UX/UI-дизайнер выполняет следующие типичные задачи: собирает данные, проводит опросы среди потребителей и анализирует полученную информацию,"
                teacher "разрабатывает пользовательские сценарии, создаёт интерактивные прототипы, тестирует и оптимизирует макеты, отрисовывает графические элементы интерфейсов."
                hide teacher
            "Какими знаниями и навыками необходимо обладать, чтобы стать UI/UX - дизайнером?" if not 2 in q:
                $ q.append(2)
                show teacher
                teacher "Чтобы хорошо справляться со своей работой, UX/UI-дизайнеру нужно обладать целым комплексом навыков."
                teacher "Знать основы разработки интерфейсов, диджитал-маркетинга, визуальный язык дизайна, быть усидчивым и креативным, а также владеть аналитическими навыками."
                hide teacher
                $ q2 = []
                while len(q2) < 2:
                    menu:
                        "А зачем нам знать основы диджитал маркетинга?" if not 1 in q2:
                            $ q2.append(1)
                            show teacher
                            teacher "Без исследования целевой аудитории создать эффективный и конкурентоспособный сайт или приложение не получится."
                            teacher "Поэтому UX/UI-дизайнер должен понимать, как составлять портрет пользователя и как исследовать продукты конкурентов."
                            hide teacher
                        "С какими программами мы должны уметь работать?" if not 2 in q2:
                            $ q2.append(2)
                            show teacher
                            teacher "Для работы вам понадобяться такие программы: Figma – для разработки прототипов и тестирования, Sketch – для создания векторной графики, "
                            teacher "Adobe XD – для разработки интерфейсов, Adobe After Effects – редактор для визуализации анимации сайта."
                            hide teacher
            "Какая заработная плата?" if not 3 in q:
                $ q.append(3)
                show teacher
                teacher "Зарплата UX/UI-дизайнера зависит от вашего профессионализма и варьируется в разных регионах страны, однако старт везде одинаковый — это примерно 60-70 тысяч тунастьёнов."
                teacher "С опытом работы от года до трех лет вы сможете зарабатывать уже выше 100 тысяч тунастьёнов."
                hide teacher
    call chapter3End from _call_chapter3End
    return

label chapter3End:
    scene bg university
    show anna normal at left2
    show margo normal at right2
    Margo "Ну что, как тебе пара?"
    Anna "Я узнала много нового об этой специальности, поэтому она еще больше меня притягивает."
    Margo "Я рада, что тебе понравилось, но мне уже пора на некст пару."
    Anna "Хорошо, удачи тебе на паре, а я пойду выпью кофе."
    return
