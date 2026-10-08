#!/usr/bin/env python3
"""소개 페이지 세 언어(index.html · ja/index.html · en/index.html)를 한 틀에서 만든다.
문구를 고치면 아래 STR을 고치고 `python3 build.py`를 다시 돌린다 — 세 파일을 손으로 고치면 언어끼리 어긋난다.
앱 화면 그림은 assets/screens/{언어}-{화면}.webp (모아냥 앱을 예시 데이터로 찍은 것)."""
from string import Template

FAQ = {
 "ko": "<h3>기록은 어디에 저장되나요?</h3>\n<p>모은 돈, 날짜별 기록, 물건 목록은 모두 내 기기에만 저장돼요. 서버에는 보내지 않아서 앱을 삭제하면 기록도 함께 사라져요. 앱을 지우거나 폰을 바꾸기 전에 <b>설정 → 백업 파일 만들기</b>로 파일을 저장해 두면, 그 파일로 언제든 되살릴 수 있어요.</p>\n<h3>필름이 뭔가요?</h3>\n<p>물건 사진을 픽셀 그림으로 바꿀 때 한 장씩 쓰여요. 처음 한 장은 무료이고, 그 뒤로는 필름 팩을 사서 쓸 수 있어요. 변환에 실패하면 필름은 돌아와요.</p>\n<h3>앱을 지웠다 다시 깔면 필름은 어떻게 되나요?</h3>\n<p>그대로 남아 있어요. 필름은 아이폰 키체인에 보관된 번호로 관리돼서 다시 설치해도 이어지고, iCloud 키체인을 켜 두면 같은 Apple 계정의 새 아이폰으로도 넘어가요. 결제했는데 필름이 들어오지 않았다면 결제한 날짜와 상품을 적어 메일로 알려 주세요.</p>\n<h3>사진은 어디로 보내지나요?</h3>\n<p>픽셀 그림으로 바꾸기 위해 외부 AI 서비스(fal.ai)로 보내지고, 저장되지 않아요. 자세한 내용은 <a href=\"privacy.html\">개인정보 처리방침</a>에 있어요.</p>\n<h3>환불은 어떻게 하나요?</h3>\n<p>결제는 Apple이 처리해서 환불도 Apple에 요청해야 해요. <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>에서 신청할 수 있어요.</p>",
 "ja": "<h3>記録はどこに保存されますか？</h3>\n<p>たまったお金、日ごとの記録、ほしいものリストはすべてこの端末にのみ保存されます。サーバーには送られないため、アプリを削除すると記録も消えます。アプリの削除や機種変更の前に<b>設定 → バックアップファイルを作る</b>でファイルを保存しておけば、そのファイルからいつでも戻せます。</p>\n<h3>フィルムとは何ですか？</h3>\n<p>写真をドット絵に変換するときに1枚ずつ使います。最初の1枚は無料で、その後はフィルムパックを購入して使えます。変換に失敗した場合、フィルムは戻ります。</p>\n<h3>アプリを入れ直すとフィルムはどうなりますか？</h3>\n<p>そのまま残ります。フィルムはiPhoneのキーチェーンに保管した番号で管理しているため、再インストールしても引き継がれ、iCloudキーチェーンをオンにしていれば同じApple アカウントの新しいiPhoneにも引き継がれます。購入後にフィルムが届かない場合は、購入日と商品を添えてメールでお問い合わせください。</p>\n<h3>写真はどこに送られますか？</h3>\n<p>ドット絵に変換するため外部のAIサービス（fal.ai）に送信され、保存されません。詳しくは<a href=\"privacy.html\">プライバシーポリシー</a>をご確認ください。</p>\n<h3>返金するには？</h3>\n<p>決済はAppleが行うため、返金もAppleにご請求ください。<a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>から申請できます。</p>",
 "en": "<h3>Where are my records stored?</h3>\n<p>Your savings, daily log, and wish list are stored only on this device. They aren’t sent to a server, so deleting the app deletes them too. Before deleting the app or switching phones, save a file with <b>Settings → Make a backup file</b> — you can restore from it anytime.</p>\n<h3>What are films?</h3>\n<p>One film is used each time a photo is turned into pixel art. Your first film is free; after that you can buy film packs. If a conversion fails, the film is returned.</p>\n<h3>What happens to my films if I reinstall the app?</h3>\n<p>They stay. Films are tied to a number kept in your iPhone’s Keychain, so they carry over when you reinstall — and to a new iPhone on the same Apple Account if iCloud Keychain is on. If films didn’t arrive after a purchase, email us with the purchase date and product.</p>\n<h3>Where do my photos go?</h3>\n<p>They’re sent to an external AI service (fal.ai) to make the pixel art and aren’t stored. See the <a href=\"privacy.html\">Privacy Policy</a> for details.</p>\n<h3>How do I get a refund?</h3>\n<p>Apple processes all payments, so refunds are requested from Apple at <a href=\"https://reportaproblem.apple.com\">reportaproblem.apple.com</a>.</p>"
}

STR = {
 'ko': dict(
  title='모아냥 — 안 쓴 돈으로 갖고 싶은 물건을 물들여요',
  desc='안 쓴 돈을 하루 한 번 적으면, 갖고 싶은 물건 사진이 모은 만큼 물들어요.',
  brand='모아냥', soon='곧 출시',
  h1='안 쓴 돈으로<br>갖고 싶은 걸<br>물들여요',
  lead='커피 한 잔, 택시 한 번. 오늘 아낀 돈을 적으면 찍어 둔 물건 사진이 모은 만큼 색으로 차올라요.',
  item='텀블러', pct='45% 모았어요', hero_bubble='오늘 아낀 돈만큼<br>사진이 물든다냥',
  hero_hand='하루 10초면 끝!', cat_alt='모아냥 고양이', tumbler_alt='픽셀 그림 텀블러',
  how='이렇게 써요',
  s1h='안 쓴 돈을 적어요', s1p='오늘 아낀 돈을 동전과 지폐를 눌러 하루 한 번 적어요. 커피든 택시든, 무엇을 아꼈든 상관없어요.', s1n='톡톡 누르고 기록!',
  s2h='갖고 싶은 걸 찍어요', s2p='사진을 찍으면 AI가 픽셀 그림 폴라로이드로 바꿔서 나무 보드에 붙여 줘요. 처음엔 흑백이에요.', s2n='내 보드에 착!',
  s3h='모은 만큼 물들어요', s3p='기록할수록 사진이 아래에서부터 색으로 차올라요. 얼마 남았는지도 바로 보여요. 다 물들면 살 수 있다는 뜻이에요.', s3n='반쯤 왔다!',
  s4h='사면 고양이를 꾸며요', s4p='물건을 사면 코인이 생겨요. 코인으로 고양이에게 모자 · 목걸이 · 안경을 씌워 줘요.', s4n='오늘은 베레모',
  calh='돌아보면 뿌듯해요', calp='기록 탭에서 날마다 얼마 아꼈는지 한눈에 봐요. 많이 아낀 날일수록 진하게, 물건을 산 날엔 그 사진이 붙어요.', caln='텀블러 산 날!',
  catsh='아낀 만큼 멋져지는 고양이', cats_bubble='모자 하나가<br>물건 하나다냥',
  cats_cap='모자 · 목걸이 · 안경 15가지. 고양이를 꾸민 만큼 실제로 산 물건이 늘어나요.',
  santa_alt='산타모자와 하트 목걸이를 한 고양이', beanie_alt='비니와 방울, 동그란 안경을 쓴 고양이', beret_alt='베레모와 목도리를 한 고양이',
  shareh='자랑하고 싶을 땐', sharep='폴라로이드와 꾸민 고양이를 예쁜 그림으로 만들어 인스타그램 스토리에 바로 올리거나 친구에게 보내요. 가격과 모은 금액을 보여줄지는 올리기 전에 고를 수 있어요.', sharen='스토리에 바로 올리기!', story_alt='인스타그램 스토리에 올린 모습',
  p1h='가입 없이 바로', p1p='이메일도 비밀번호도 없어요. 켜자마자 써요.',
  p2h='기록은 내 폰에만', p2p='모은 돈과 기록은 서버로 보내지 않아요. 백업 파일로 직접 챙길 수 있어요.',
  p3h='광고 없음', p3p='화면을 가리는 광고가 없어요. 첫 사진 한 장은 무료예요.',
  faqh='자주 묻는 질문', contact='문의', privacy='개인정보 처리방침',
  shot_alt='모아냥 앱 화면',
 ),
 'ja': dict(
  title='モアニャン — 使わなかったお金で、ほしいものに色をつけよう',
  desc='使わなかったお金を1日1回記録すると、ほしいものの写真がたまったぶんだけ色づきます。',
  brand='モアニャン', soon='近日公開',
  h1='使わなかったお金で<br>ほしいものに<br>色をつけよう',
  lead='コーヒー1杯、タクシー1回。今日節約したお金を記録すると、撮っておいたほしいものの写真が、たまったぶんだけ色づきます。',
  item='タンブラー', pct='45%たまりました', hero_bubble='節約したぶんだけ<br>写真が色づくにゃ',
  hero_hand='1日10秒でおしまい!', cat_alt='モアニャンのねこ', tumbler_alt='ドット絵のタンブラー',
  how='使い方',
  s1h='使わなかったお金を記録', s1p='今日節約したお金を、硬貨とお札を押して1日1回記録します。コーヒーでもタクシーでも、何を節約したかは問いません。', s1n='ポチッと記録!',
  s2h='ほしいものを撮る', s2p='写真を撮ると、AIがドット絵のインスタント写真にして木のボードに貼ってくれます。最初は白黒です。', s2n='ボードにペタッ!',
  s3h='ためたぶんだけ色づく', s3p='記録するほど、写真が下から色で満ちていきます。あといくらかもすぐわかります。全部色づいたら、買えるという合図です。', s3n='半分まできた!',
  s4h='買ったら、ねこをおしゃれに', s4p='買うとコインがもらえます。コインで、ねこに帽子・ネックレス・メガネをつけてあげられます。', s4n='今日はベレー帽',
  calh='ふりかえると、うれしい', calp='記録タブで、毎日いくら節約したかがひと目でわかります。たくさん節約した日ほど濃く、買った日にはその写真が貼られます。', caln='タンブラーを買った日!',
  catsh='節約するほど、おしゃれになるねこ', cats_bubble='帽子ひとつが<br>買えたものひとつにゃ',
  cats_cap='帽子・ネックレス・メガネ、全15種類。ねこがおしゃれになったぶん、実際に買えたものが増えていきます。',
  santa_alt='サンタ帽とハートのネックレスをつけたねこ', beanie_alt='ニット帽と鈴、丸メガネのねこ', beret_alt='ベレー帽とマフラーをつけたねこ',
  shareh='自慢したくなったら', sharep='インスタント写真やおしゃれしたねこを、きれいな画像にしてInstagramのストーリーズにそのまま投稿したり、友だちに送ったりできます。値段やためた金額を表示するかは、投稿前に選べます。', sharen='ストーリーズにそのまま!', story_alt='Instagramのストーリーズに投稿したところ',
  p1h='登録なしですぐ使える', p1p='メールアドレスもパスワードもいりません。開いたらすぐ使えます。',
  p2h='記録はスマホの中だけ', p2p='たまったお金や記録はサーバーに送りません。バックアップファイルで自分で守れます。',
  p3h='広告なし', p3p='画面をふさぐ広告はありません。最初の1枚は無料です。',
  faqh='よくある質問', contact='お問い合わせ', privacy='プライバシーポリシー',
  shot_alt='モアニャンのアプリ画面',
 ),
 'en': dict(
  title='MoaNyang — Color in what you want with money you didn’t spend',
  desc='Log the money you didn’t spend once a day, and a photo of what you want fills with color as you save.',
  brand='MoaNyang', soon='Coming soon',
  h1='Skip it.<br>Save it.<br>Color it in.',
  lead='A coffee here, a cab ride there. Log what you saved today, and the photo of what you want fills with color as you go.',
  item='Tumbler', pct='45% saved', hero_bubble='Save a little,<br>color a little, meow',
  hero_hand='10 seconds a day!', cat_alt='The MoaNyang cat', tumbler_alt='Pixel-art tumbler',
  how='How it works',
  s1h='Log what you didn’t spend', s1p='Tap coins and bills to log what you saved, once a day. Coffee, a cab ride — whatever you skipped counts.', s1n='tap, tap, done!',
  s2h='Snap what you want', s2p='AI turns your photo into a pixel-art snapshot and pins it to your wooden board. It starts out black and white.', s2n='pinned to my board!',
  s3h='It fills as you save', s3p='The more you log, the higher the color rises — and you can see exactly how much is left. When it’s full, you can afford it.', s3n='halfway there!',
  s4h='Buy it, dress your cat', s4p='Buying earns coins. Spend them on hats, necklaces and glasses for your cat.', s4n='beret day',
  calh='Look back and smile', calp='The History tab shows how much you saved each day. Bigger days get darker, and the days you bought something get its photo.', caln='bought the tumbler!',
  catsh='The more you save, the fancier the cat', cats_bubble='Every hat is<br>a thing you bought, meow',
  cats_cap='15 hats, necklaces and glasses. The fancier your cat, the more you’ve actually bought.',
  santa_alt='Cat in a Santa hat and heart necklace', beanie_alt='Cat in a beanie, bell and round glasses', beret_alt='Cat in a beret and scarf',
  shareh='Show it off', sharep='Turn your snapshot or dressed-up cat into a clean image and post it straight to your Instagram Story, or send it to a friend. Choose whether to show the price or your total before you share.', sharen='straight to your Story!', story_alt='Posted to an Instagram Story',
  p1h='No sign-up', p1p='No email, no password. Open it and go.',
  p2h='Your records stay on your phone', p2p='Your savings and logs are never sent to a server. Keep them safe with a backup file.',
  p3h='No ads', p3p='Nothing covers your screen. Your first photo is free.',
  faqh='FAQ', contact='Contact', privacy='Privacy Policy',
  shot_alt='MoaNyang app screen',
 ),
}

PAGE = Template(r"""<!doctype html>
<html lang="$lang">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$desc">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=$hand_font&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="${up}favicon.png">
<link rel="stylesheet" href="${up}landing.css">
</head>
<body>
<div class="board">
  <header class="top">
    <a class="logo" href="${home}"><img src="${up}assets/icon.png" alt="" width="40" height="40">$brand</a>
    <nav>$nav</nav>
  </header>

  <!-- ① 첫 화면: 제목 쪽지 · 앱 화면 · 물드는 폴라로이드 · 고양이 -->
  <section class="hero">
    <div class="note">
      <span class="tape" style="--tape-rot: 3deg"></span>
      <h1>$h1</h1>
      <p>$lead</p>
      <span class="soon">App Store <small>$soon</small></span>
    </div>

    <div class="hero-stage">
      <figure class="phone" style="--rot: 3deg">
        <span class="tape"></span>
        <img src="${up}assets/screens/$lang-home.webp" alt="$shot_alt" width="600" height="1299">
      </figure>
      <!-- 처음엔 흑백, 페이지가 열리면 아래에서부터 45%까지 물든다(앱의 대표 순간) -->
      <div class="pol hero-pol" id="hero-pol" style="--rot: -6deg">
        <span class="tape"></span>
        <div class="win">
          <img src="${up}assets/onboarding-tumbler.png" alt="$tumbler_alt">
          <img class="gray" src="${up}assets/onboarding-tumbler.png" alt="" aria-hidden="true">
        </div>
        <div class="lab"><b>$item</b><i>$pct</i></div>
      </div>
      <p class="hand hero-hand">$hero_hand</p>
      <svg class="arrow hero-arrow" viewBox="0 0 120 80" aria-hidden="true"><path d="M8 12c30 4 66 18 88 52"/><path d="M80 58l17 8 2-19"/></svg>
    </div>

    <div class="cat">
      <p class="bubble">$hero_bubble</p>
      <img src="${up}assets/cat-hero.png" alt="$cat_alt">
    </div>
  </section>

  <!-- ② 이렇게 써요: 앱 화면과 설명이 지그재그로 -->
  <section class="section">
    <h2 class="section-title">$how</h2>
    <ol class="flow">
$steps
    </ol>
  </section>

  <!-- ③ 기록 탭 -->
  <section class="section">
    <div class="feature">
      <figure class="phone" style="--rot: -2.5deg">
        <span class="tape"></span>
        <img src="${up}assets/screens/$lang-history.webp" alt="$shot_alt" width="600" height="1299" loading="lazy">
      </figure>
      <div class="card" style="--rot: 1deg">
        <h2>$calh</h2>
        <p>$calp</p>
        <p class="hand">$caln</p>
      </div>
    </div>
  </section>

  <!-- ④ 고양이 꾸미기 -->
  <section class="section">
    <h2 class="section-title">$catsh</h2>
    <div class="cats">
      <figure><img src="${up}assets/cat-santa.png" alt="$santa_alt" loading="lazy"></figure>
      <figure class="cats-mid">
        <p class="bubble">$cats_bubble</p>
        <img src="${up}assets/cat-beanie.png" alt="$beanie_alt" loading="lazy">
      </figure>
      <figure><img src="${up}assets/cat-beret.png" alt="$beret_alt" loading="lazy"></figure>
    </div>
    <p class="cats-caption">$cats_cap</p>
  </section>

  <!-- ⑤ 공유: 앱이 만드는 공유 그림을 스토리 화면에 올린 모습 -->
  <section class="section">
    <div class="share">
      <div class="stories">
        <figure class="story" style="--rot: -4deg">
          <span class="story-bar"><i></i><i></i></span>
          <span class="story-who"><img src="${up}assets/icon.png" alt="">$brand</span>
          <img class="story-img" src="${up}assets/share/$lang-pol.webp" alt="$story_alt" loading="lazy">
        </figure>
        <figure class="story" style="--rot: 3deg">
          <span class="story-bar"><i></i><i></i></span>
          <span class="story-who"><img src="${up}assets/icon.png" alt="">$brand</span>
          <img class="story-img" src="${up}assets/share/$lang-cat.webp" alt="$story_alt" loading="lazy">
        </figure>
      </div>
      <div class="card" style="--rot: -1deg">
        <h2>$shareh</h2>
        <p>$sharep</p>
        <p class="hand">$sharen</p>
      </div>
    </div>
  </section>

  <!-- ⑥ 약속 세 가지: 메모지 -->
  <section class="section">
    <ul class="promises">
      <li style="--rot: -2deg"><span class="pin"></span><b>$p1h</b><span>$p1p</span></li>
      <li style="--rot: 1.5deg"><span class="pin"></span><b>$p2h</b><span>$p2p</span></li>
      <li style="--rot: -1deg"><span class="pin"></span><b>$p3h</b><span>$p3p</span></li>
    </ul>
  </section>

  <!-- ⑦ 자주 묻는 질문 · 문의 (지원 페이지) -->
  <section class="section" id="faq">
    <div class="sheet">
      <span class="tape"></span>
      <h2>$faqh</h2>
$faq
      <p class="contact">$contact <a href="mailto:sokurihj@gmail.com">sokurihj@gmail.com</a></p>
    </div>
  </section>

  <footer class="foot">$brand · <a href="privacy.html">$privacy</a> · <a href="mailto:sokurihj@gmail.com">sokurihj@gmail.com</a></footer>
</div>
<script>
  // 첫 그림을 그린 뒤에 값을 바꿔야 CSS 전환이 걸린다(처음부터 0.45면 물드는 모습이 안 보인다).
  requestAnimationFrame(() => requestAnimationFrame(() => document.getElementById('hero-pol').classList.add('filled')));
  // 아래 칸의 앱 화면·쪽지는 화면에 들어올 때 살짝 떠오른다(한 번만).
  const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.2 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
</script>
</body>
</html>
""")

STEP = Template("""      <li class="flow-row reveal">
        <figure class="$shot_class" style="--rot: $rot">
          <span class="tape"></span>
          <img src="${up}assets/screens/$lang-$screen.webp" alt="$shot_alt" loading="lazy">$extra
        </figure>
        <div class="card" style="--rot: $crot">
          <span class="stamp">$num</span>
          <h3>$h</h3>
          <p>$p</p>
          <p class="hand">$n</p>
        </div>
      </li>""")

HAND = {'ko': 'Nanum+Pen+Script', 'ja': 'Yomogi', 'en': 'Caveat:wght@600'}
NAV = {'ko': ('./', 'ja/', 'en/'), 'ja': ('../', './', '../en/'), 'en': ('../', '../ja/', './')}

for lang, s in STR.items():
    up = '' if lang == 'ko' else '../'
    links = NAV[lang]
    nav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if l == lang else ""}>{n}</a>'
                  for h, l, n in zip(links, ('ko', 'ja', 'en'), ('한국어', '日本語', 'English')))
    steps = '\n'.join(STEP.substitute(up=up, lang=lang, shot_alt=s['shot_alt'], num=f'0{i}', h=s[f's{i}h'], p=s[f's{i}p'], n=s[f's{i}n'],
                                      screen=scr, shot_class=cls, rot=rot, crot=crot,
                                      extra=f'\n          <img class="flow-cat" src="{up}assets/cat-beret.png" alt="{s["beret_alt"]}" loading="lazy">' if scr == 'shop' else '')
                      for i, (scr, cls, rot, crot) in enumerate([('entry', 'phone', '-2deg', '1deg'), ('board', 'snap', '2deg', '-1deg'),
                                                                 ('detail', 'phone', '2.5deg', '-1.2deg'), ('shop', 'phone', '-1.5deg', '1.4deg')], 1))
    faq = '\n'.join('      ' + l for l in FAQ[lang].splitlines())
    html = PAGE.substitute(s, lang=lang, up=up, home=links[('ko', 'ja', 'en').index(lang)], nav=nav, steps=steps, faq=faq, hand_font=HAND[lang])
    open('index.html' if lang == 'ko' else f'{lang}/index.html', 'w').write(html)
    print('wrote', lang)
