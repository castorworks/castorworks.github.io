#!/usr/bin/env python3
"""Writes the site's pages. Run it after changing the text below; the HTML it writes is what gets served."""
from pathlib import Path

EMAIL = "riclavaz@gmail.com"
COPYRIGHT = "© 2026 Chongqing Hyperits Network Technology Co., Ltd."

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="/screenshoteasy/icon.png">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<main>
<header>
<img src="/screenshoteasy/icon.png" alt="">
<div><h1>ScreenshotEasy</h1><p>{tagline}</p></div>
</header>
<nav>
<a href="{support_url}"{support_current}>{support_label}</a>
<a href="{privacy_url}"{privacy_current}>{privacy_label}</a>
<span class="spacer"></span>
<a href="{other_url}" lang="{other_lang}">{other_label}</a>
</nav>
{body}
<footer>{copyright}</footer>
</main>
</body>
</html>
"""

TEXT = {
    "en": dict(
        lang="en", tagline="Capture, annotate, pin, and recognize text on your Mac",
        support_label="Support", privacy_label="Privacy Policy", other_label="简体中文", other_lang="zh-Hans",
        support_title="ScreenshotEasy Support", support_description="Help and contact for ScreenshotEasy, a screenshot tool for macOS.",
        privacy_title="ScreenshotEasy Privacy Policy", privacy_description="ScreenshotEasy does not collect, transmit, or share any data.",
        support=f"""<h2>Getting started</h2>
<p>ScreenshotEasy lives in the menu bar and has no Dock icon. Click its icon in the menu bar, or press <kbd>⌃⌘A</kbd> to capture a region and <kbd>⌃⇧3</kbd> to capture the full screen.</p>

<h2>Common questions</h2>
<h3>Nothing happens when I capture, or the capture is blank</h3>
<p>macOS needs your permission before an app can read the screen. Open System Settings → Privacy &amp; Security → Screen &amp; System Audio Recording, turn on ScreenshotEasy, then quit and reopen the app.</p>
<h3>A shortcut doesn’t work</h3>
<p>Another app may be using the same keys. Open Settings from the menu bar icon and record a different shortcut, or clear the one that conflicts.</p>
<h3>Where do my screenshots go?</h3>
<p>To the clipboard. A file is written only when you choose Save, by default into <code>~/Pictures/ScreenshotEasy</code>. You can pick another folder and switch between PNG and JPEG in Settings.</p>
<h3>How do I capture a menu or a tooltip that disappears?</h3>
<p>Use Capture After Delay in the menu bar menu. You get 3 or 5 seconds to open the menu before the screen is captured.</p>
<h3>How do I close or move a pinned screenshot?</h3>
<p>Drag it to move it and scroll over it to zoom. Double-click it, or press <kbd>Esc</kbd> while the pointer is over it, to close it. Right-click it for opacity and actual size.</p>
<h3>Which languages does text recognition support?</h3>
<p>Chinese (Simplified and Traditional) and English. Recognition runs on your Mac.</p>
<h3>How do I turn off the list of recent screenshots?</h3>
<p>Turn off “Keep recent screenshots” in Settings. The captures already kept are deleted at the same time.</p>
<h3>How do I change the app’s language?</h3>
<p>Choose one under Language in Settings. It takes effect right away.</p>

<div class="contact">
<h2>Contact</h2>
<p>If something isn’t working or you have a suggestion, write to <a href="mailto:{EMAIL}">{EMAIL}</a>. Including your macOS version and what you were doing helps a lot.</p>
</div>""",
        privacy=f"""<h2>Privacy Policy</h2>
<p>Last updated: October 9, 2026</p>
<p>ScreenshotEasy does not collect, transmit, or share any data.</p>
<ul>
<li><strong>No network access.</strong> The app never connects to the internet. It has no account system, no analytics, no advertising, and no third-party tracking.</li>
<li><strong>Screen content.</strong> The app reads your screen only when you start a capture. This requires the Screen Recording permission, which you grant in System Settings and can revoke at any time.</li>
<li><strong>Where captures go.</strong> A capture is placed on the clipboard. It is written to a file only when you choose Save, in the folder you selected.</li>
<li><strong>History.</strong> If “Keep recent screenshots” is on, your last 20 captures are stored inside the app’s own sandbox container on your Mac. Turning the setting off deletes them.</li>
<li><strong>Text recognition.</strong> Text is recognized on your Mac with Apple’s Vision framework. Nothing is uploaded.</li>
</ul>
<p>Deleting the app and its container removes everything it has stored.</p>

<div class="contact">
<h2>Contact</h2>
<p>Questions about this policy: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>""",
    ),
    "zh": dict(
        lang="zh-Hans", tagline="Mac 上的截图、标注、钉图与文字识别工具",
        support_label="技术支持", privacy_label="隐私政策", other_label="English", other_lang="en",
        support_title="ScreenshotEasy 技术支持", support_description="macOS 截图工具 ScreenshotEasy 的使用帮助与联系方式。",
        privacy_title="ScreenshotEasy 隐私政策", privacy_description="ScreenshotEasy 不收集、不传输、不共享任何数据。",
        support=f"""<h2>开始使用</h2>
<p>ScreenshotEasy 常驻菜单栏，没有 Dock 图标。点击菜单栏上的图标，或按 <kbd>⌃⌘A</kbd> 区域截图、<kbd>⌃⇧3</kbd> 全屏截图。</p>

<h2>常见问题</h2>
<h3>截图没有反应，或者截出来是空白</h3>
<p>应用读取屏幕内容之前需要你的授权。打开“系统设置 → 隐私与安全性 → 录屏与系统录音”，打开 ScreenshotEasy 的开关，然后退出并重新打开应用。</p>
<h3>快捷键不起作用</h3>
<p>可能有其他应用占用了同样的按键。从菜单栏图标打开“设置”，重新录制一个快捷键，或者清除冲突的那个。</p>
<h3>截图保存到哪里了？</h3>
<p>截图默认只进剪贴板。只有在你选择“保存”时才会写入文件，默认位置是 <code>~/Pictures/ScreenshotEasy</code>。保存位置和格式（PNG 或 JPEG）可以在设置里更改。</p>
<h3>怎么截取一动鼠标就消失的菜单或提示？</h3>
<p>使用菜单栏菜单里的“延时截图”。你有 3 秒或 5 秒的时间先把菜单打开，然后才会截屏。</p>
<h3>钉在屏幕上的截图怎么移动和关闭？</h3>
<p>拖动可以移动，滚轮可以缩放。双击，或者鼠标悬停在上面时按 <kbd>Esc</kbd>，可以关闭。右键菜单里可以调整不透明度、恢复实际大小。</p>
<h3>文字识别支持哪些语言？</h3>
<p>中文（简体和繁体）和英文。识别全程在本机完成。</p>
<h3>怎么关闭“最近的截图”？</h3>
<p>在设置里关闭“保留最近的截图”。已经保留的截图会同时被删除。</p>
<h3>怎么更改应用的语言？</h3>
<p>在设置的“语言”里选择，立即生效。</p>

<div class="contact">
<h2>联系我们</h2>
<p>遇到问题或者有建议，请发邮件到 <a href="mailto:{EMAIL}">{EMAIL}</a>。附上 macOS 版本和当时的操作，会更容易定位问题。</p>
</div>""",
        privacy=f"""<h2>隐私政策</h2>
<p>最后更新：2026 年 10 月 9 日</p>
<p>ScreenshotEasy 不收集、不传输、不共享任何数据。</p>
<ul>
<li><strong>不联网。</strong>应用从不连接互联网，没有账号系统，没有数据统计，没有广告，也没有第三方追踪。</li>
<li><strong>屏幕内容。</strong>只有在你发起截图时，应用才会读取屏幕内容。这需要屏幕录制权限，由你在系统设置中授予，并可随时撤销。</li>
<li><strong>截图去向。</strong>截图会放入剪贴板。只有在你选择保存时，才会写入你指定的文件夹。</li>
<li><strong>历史记录。</strong>开启“保留最近的截图”时，最近 20 张截图保存在本机的应用沙盒容器内。关闭该设置会将其删除。</li>
<li><strong>文字识别。</strong>文字识别通过 Apple 的 Vision 框架在本机完成，不会上传任何内容。</li>
</ul>
<p>删除应用及其容器即可清除它保存的全部内容。</p>

<div class="contact">
<h2>联系方式</h2>
<p>对本政策有疑问，请联系 <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>""",
    ),
}

ROOTS = {"en": "/screenshoteasy/", "zh": "/screenshoteasy/zh/"}


def write(path: str, content: str) -> None:
    file = Path(__file__).parent / path.strip("/") / "index.html"
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding="utf-8")


for language, text in TEXT.items():
    other = "zh" if language == "en" else "en"
    for kind in ("support", "privacy"):
        suffix = "" if kind == "support" else "privacy/"
        write(ROOTS[language] + suffix, PAGE.format(
            lang=text["lang"], title=text[f"{kind}_title"], description=text[f"{kind}_description"],
            tagline=text["tagline"], body=text[kind], copyright=COPYRIGHT,
            support_url=ROOTS[language], support_label=text["support_label"],
            support_current=' aria-current="page"' if kind == "support" else "",
            privacy_url=ROOTS[language] + "privacy/", privacy_label=text["privacy_label"],
            privacy_current=' aria-current="page"' if kind == "privacy" else "",
            other_url=ROOTS[other] + suffix, other_lang=text["other_lang"], other_label=text["other_label"],
        ))

(Path(__file__).parent / "index.html").write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CastorWorks</title>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<main>
<h2>Apps</h2>
<ul>
<li><a href="/zuneyra/">Zuneyra</a>: your personal offline music collection</li>
<li><a href="/screenshoteasy/">ScreenshotEasy</a>: capture, annotate, pin, and recognize text on your Mac</li>
</ul>
<footer>{COPYRIGHT}</footer>
</main>
</body>
</html>
""", encoding="utf-8")
