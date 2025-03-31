# ഫാസ്റ്റ് API

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="ഫാസ്റ്റ് API"></a>
</p>
<p align="center">
    <em>ഫാസ്റ്റ് API ഫ്രെയിംവർക്ക്, ഉയർന്ന പ്രകടനം, പഠിക്കാൻ എളുപ്പം, നിർമ്മാണത്തിന് തയ്യാറാണ് </em>
</p>
<p align="center">
<a href="https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**ഡോക്യുമെൻ്റേഷൻ**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**സോഴ്സ് കോഡ്**: <a href="https://github.com/fastapi/fastapi" target="_blank">https://github.com/fastapi/fastapi</a>

---


ഫാസ്റ്റ് API ഒരു ആധുനികവും വേഗതയേറിയതുമായ (ഉയർന്ന പ്രകടനക്ഷമതയുള്ള) വെബ് ഫ്രെയിംവർക്ക് ആണ്, ഇത് സ്റ്റാൻഡേർഡ് പൈത്തൺ ടൈപ്പ് ഹിന്റ്സ് അടിസ്ഥാനമാക്കി പൈത്തണിൽ APIകൾ നിർമ്മിക്കാൻ വികസിപ്പിച്ചെടുത്തിരിക്കുന്നു.

പ്രധാന സവിശേഷതകൾ ഇവയാണ്:

* **വേഗതയുള്ള**: വളരെ ഉയർന്ന പ്രകടനം, **NodeJS**, **Go** എന്നിവയ്ക്ക് തുല്യമായി (സ്റ്റാർലെറ്റിനും പൈഡൻ്റിക്കിനും നന്ദി). [ ലഭ്യമായ ഏറ്റവും വേഗമേറിയ പൈത്തൺ ഫ്രെയിംവർക്കുകളിൽ ഒന്നു ](#പർഫോർമൻസ്).
* **വേഗത്തിൽ കോഡ് ചെയ്യാം**: സവിശേഷതകൾ വികസിപ്പിക്കുന്നതിനുള്ള വേഗത ഏകദേശം 200% മുതൽ 300% വരെ വർദ്ധിപ്പിക്കുന്നു. *
* **കുറവ് ബഗുകൾ**: മാനുഷിക (ഡെവലപ്പർ) പ്രേരിത പിശകുകളുടെ ഏകദേശം 40% കുറയ്ക്കുന്നു.  *
* **അവബോധജന്യമായ**: മികച്ച എഡിറ്റർ പിന്തുണ. <abbr title="ഓട്ടോ-കമ്പ്ലീറ്റ്, ഓട്ടോക്കംപ്ലീഷൻ, ഇൻ്റലിസെൻസ് എന്നും അറിയപ്പെടുന്നു"> പൂർത്തീകരണം</abbr> എല്ലായിടത്തും. ചുരുങ്ങിയ സമയത്തിൽ  ഡീബഗ്ഗിംഗ്.
* **എളുപ്പം**: എളുപ്പത്തിൽ ഉപയോഗിക്കാനും പഠിക്കാനും രൂപകൽപ്പന ചെയ്തിരിക്കുന്നത്. കുറഞ്ഞ സമയം കൊണ്ട് ഡോക്യുമെന്റേഷൻ വായിക്കാം.
* **ലഘു**: കോഡ് ഡ്യൂപ്ലിക്കേഷൻ കുറയ്ക്കുക. ഓരോ പാരാമീറ്റർ പ്രഖ്യാപനത്തിൽ നിന്നും ഒന്നിലധികം സവിശേഷതകൾ. കുറച്ച് ബഗുകൾ.
* **കരുത്തുള്ള**: ഓട്ടോമാറ്റിക് ഇൻ്ററാക്ടീവ് ഡോക്യുമെൻ്റേഷൻ ഉപയോഗിച്ച് നിർമ്മാണത്തിന് തയ്യാറായ കോഡ് ലഭിക്കും.
* **മാനദണ്ഡങ്ങൾ അടിസ്ഥാനമാക്കിയുള്ളത്**: API-കൾക്കുള്ള ഓപ്പൺ സ്റ്റാൻഡേർഡുകളെ അടിസ്ഥാനമാക്കി (പൂർണമായും പൊരുത്തപ്പെടുന്നു): <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">ഓപ്പൺ API</a> (മുമ്പ് സ്വാഗർ എന്നറിയപ്പെട്ടിരുന്നു) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON സ്കീമ</a>.

<small>* പ്രൊഡക്ഷൻ ആപ്ലിക്കേഷനുകൾ വികസിപ്പിക്കുന്ന ഒരു ഇൻറേണൽ ഡെവലപ്‌മെൻറ് ടീമിലെ ടെസ്റ്റുകളെ അടിസ്ഥാനമാക്കിയുള്ള മൂല്യനിർണ്ണയം. "</small>

## Sponsors

<!-- sponsors -->

{% if sponsors %}
{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor -%}
{%- for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

<!-- /sponsors -->

<a href="https://fastapi.tiangolo.com/fastapi-people/#sponsors" class="external-link" target="_blank">Other sponsors</a>

## അഭിപ്രായങ്ങൾ

"_[...] ഞാൻ ഇക്കാലത്ത് **ഫാസ്റ്റ് API** ധാരാളം ഉപയോഗിക്കുന്നുണ്ട്. [...] മൈക്രോസോഫ്റ്റിലെ എന്റെ ടീമിന്റെ എല്ലാ **ML സേവനങ്ങൾക്കും** ഇത് ഉപയോഗിക്കാൻ ഞാൻ പദ്ധതിയിടുന്നു. അവയിൽ ചിലത് കോർ **വിൻഡോസ്** ഉൽപ്പന്നത്തിലും ചില **ഓഫീസ്** ഉൽപ്പന്നങ്ങളിലും സംയോജിപ്പിക്കപ്പെടുന്നു._"

<div style="text-align: right; margin-right: 10%;">കബീർ ഖാൻ - <strong>മൈക്രോസോഫ്റ്റ്</strong> <a href="https://github.com/fastapi/fastapi/pull/26" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

"_**പ്രവചനങ്ങൾ** ലഭിക്കുന്നതിനായി അന്വേഷിക്കാൻ കഴിയുന്ന ഒരു **REST** സെർവർ നിർമ്മിക്കുന്നതിനായി ഞങ്ങൾ **ഫാസ്റ്റ് API** ലൈബ്രറി സ്വീകരിച്ചു. [ലുഡ്‌വിഗിന്]_"

<div style="text-align: right; margin-right: 10%;">പൈറോ മോളിന, യാരോസ്ലാവ് ഡുഡിൻ, സായ് സുമന്ത് മിര്യാല - <strong>യൂബർ</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

"_**നെറ്റ്ഫ്ലിക്സ്** ഞങ്ങളുടെ **ക്രൈസിസ് മാനേജ്മെന്റ്** ഓർക്കസ്ട്രേഷൻ ഫ്രെയിംവർക്കിന്റെ ഓപ്പൺ സോഴ്‌സ് റിലീസ് പ്രഖ്യാപിക്കുന്നതിൽ സന്തോഷമുണ്ട്: **ഡിസ്പാച്ച്**! [**ഫാസ്റ്റ് API** ഉപയോഗിച്ച് നിർമ്മിച്ചത്]_"

<div style="text-align: right; margin-right: 10%;">കെവിൻ ഗ്ലിസൻ, മാർക്ക് വിലനോവ, ഫോറസ്റ്റ് മോൺസെൻ - <strong>നെറ്റ്ഫ്ലിക്സ്</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

"_ഫാസ്റ്റ് API വളരെ ആവേശകരമാണ്. ഇത് വളരെ രസകരമാണ്!_"

<div style="text-align: right; margin-right: 10%;">ബ്രയാൻ ഒക്കെൻ - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">പൈത്തൺ  ബൈറ്റ്</a> പോഡ്‌കാസ്റ്റ് അവതാരകൻ</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

"_സത്യം പറഞ്ഞാൽ, നിങ്ങൾ നിർമ്മിച്ചത് വളരെ ഉറച്ചതും മിനുസപ്പെടുത്തിയതുമായി തോന്നുന്നു. പല തരത്തിൽ, **ആലിംഗനം** ആകണമെന്ന് ഞാൻ ആഗ്രഹിച്ചത് അതാണ് - ആരെങ്കിലും അത് നിർമ്മിക്കുന്നത് കാണുന്നത് ശരിക്കും പ്രചോദനം നൽകുന്നു._"

<div style="text-align: right; margin-right: 10%;">തിമോത്തി ക്രോസ്ലി - <strong><a href="https://github.com/hugapi/hug" target="_blank">ആലിംഗനം</a> creator</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

"_റെസ്റ്റ് API-കൾ നിർമ്മിക്കുന്നതിനുള്ള ഒരു **ആധുനിക ഫ്രെയിംവർക്ക്** പഠിക്കാൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, **ഫാസ്റ്റ് API** പരിശോധിക്കുക [...] വേഗതയുള്ളതും ഉപയോഗിക്കാൻ എളുപ്പമുള്ളതും പഠിക്കാൻ എളുപ്പവുമാണ് [...]_"

"_ഞങ്ങളുടെ **API-കൾക്കായി **ഫാസ്റ്റ് API**-ലേക്ക് മാറിയിരിക്കുന്നു** [...] നിങ്ങൾക്ക് ഇത് ഇഷ്ടപ്പെടുമെന്ന് ഞാൻ കരുതുന്നു [...]_"

<div style="text-align: right; margin-right: 10%;">ഇനെസ് മൊണ്ടാനി - മാത്യു ഹോണിബൽ - <strong><a href="https://explosion.ai" target="_blank">എക്സ്പ്ലോഷൻ AI</a> സ്ഥാപകർ - <a href="https://spacy.io" target="_blank">സ്പേസി</a> സ്രഷ്ടാക്കൾ</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(റഫറൻസ്)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

"_ആരെങ്കിലും ഒരു പ്രൊഡക്ഷൻ പൈത്തൺ API നിർമ്മിക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, ഞാൻ **FastAPI** ശുപാർശ ചെയ്യുന്നു. ഇത് **മനോഹരമായി രൂപകൽപ്പന ചെയ്‌തിരിക്കുന്നു**, **ഉപയോഗിക്കാൻ ലളിതമാണ്**, **ഉയർന്ന തോതിൽ സ്കെയിലബിൾ**, ഇത് ഞങ്ങളുടെ API ഫസ്റ്റ് ഡെവലപ്‌മെന്റ് തന്ത്രത്തിലെ **പ്രധാന ഘടകമായി** മാറിയിരിക്കുന്നു കൂടാതെ ഞങ്ങളുടെ വെർച്വൽ TAC എഞ്ചിനീയർ പോലുള്ള നിരവധി ഓട്ടോമേഷനുകളും സേവനങ്ങളും നയിക്കുന്നു._"

<div style="text-align: right; margin-right: 10%;">ഡിയോൺ പിൽസ്ബറി - <strong>സിസ്കോ</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/" target="_blank"><small>(റഫറൻസ്)</small></a></div>

---

## **ടൈപ്പർ**, CLI-കളുടെ ഫാസ്റ്റ് API

<a href="https://typer.tiangolo.com" target="_blank"><img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

വെബ് API-യ്ക്ക് പകരം ടെർമിനലിൽ ഉപയോഗിക്കുന്നതിനായി <abbr title="Command Line Interface">CLI</abbr> ആപ്പ് നിർമ്മിക്കുകയാണെങ്കിൽ, <a href="https://typer.tiangolo.com/" class="external-link" target="_blank">**Typer**</a> പരിശോധിക്കുക.

**ടൈപ്പർ** എന്നത് ഫാസ്റ്റ് API യുടെ ഇളയ സഹോദരനാണ്. CLI-കളുടെ **ഫാസ്റ്റ് API** ആകാനാണ് ഇത് ഉദ്ദേശിക്കുന്നത്. ⌨️ 🚀

## ആവശ്യമായത്

ഫാസ്റ്റ് API ഭീമന്മാരുടെ തോളിൽ നിൽക്കുന്നു:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">സ്റ്റാർലെറ്റ്</a> വെബ് ഭാഗങ്ങൾക്കായി.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">പൈഡാൻറിക്</a> ഡാറ്റ ഭാഗങ്ങൾക്കായി.

## ഇൻസ്റ്റലേഷൻ

ഒരു <a href="https://fastapi.tiangolo.com/virtual-environments/" class="external-link" target="_blank">വെർച്വൽ എൻവയോൺമെന്റ്</a> സൃഷ്ടിച്ച് സജീവമാക്കുക, തുടർന്ന് ഫാസ്റ്റ് API ഇൻസ്റ്റാൾ ചെയ്യുക:
<div class="termy">

```console
$ pip install "fastapi[standard]"

---> 100%
```

</div>

**കുറിപ്പ്**: എല്ലാ ടെർമിനലുകളിലും ഇത് പ്രവർത്തിക്കുന്നുവെന്ന് ഉറപ്പാക്കാൻ ഉദ്ധരണികളിൽ `"fastapi[standard]"` എന്ന് ചേർത്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക.

## ഉദാഹരണം

### സൃഷ്ടിക്കൂ

* `main.py` എന്ന ഫയൽ സൃഷ്ടിക്കുക:

```Python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>Or use <code>async def</code>...</summary>

നിങ്ങളുടെ കോഡ് `async` / `await` ഉപയോഗിക്കുകയാണെങ്കിൽ, `async def` ഉപയോഗിക്കുക:

```Python hl_lines="9  14"
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

**കുറിപ്പ്**:

നിങ്ങൾക്ക് അറിയില്ലെങ്കിൽ, ഡോക്യുമെന്റിലെ <a href="https://fastapi.tiangolo.com/async/#in-a-hurry" target="_blank">`async` ഉം `wait` ഉം</a> എന്നതിനെക്കുറിച്ചുള്ള _"തിരക്കിലാണ്?"_ വിഭാഗം പരിശോധിക്കുക.

</details>

### പ്രവർത്തിപ്പിക്കുക

സെർവർ ഇതുപയോഗിച്ച് പ്രവർത്തിപ്പിക്കുക:

<div class="termy">

```console
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary> <code>fastapi dev main.py</code> കമാൻഡിനെക്കുറിച്ച്...</summary>

`fastapi dev` എന്ന കമാൻഡ് നിങ്ങളുടെ `main.py` ഫയൽ വായിക്കുകയും അതിലെ **FastAPI** ആപ്പ് കണ്ടെത്തുകയും <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> ഉപയോഗിച്ച് ഒരു സെർവർ ആരംഭിക്കുകയും ചെയ്യുന്നു.

ഡിഫോൾട്ടായി, പ്രാദേശിക വികസനത്തിനായി പ്രവർത്തനക്ഷമമാക്കിയ ഓട്ടോ-റീലോഡ് ഉപയോഗിച്ചായിരിക്കും `fastapi dev` ആരംഭിക്കുക.

<a href="https://fastapi.tiangolo.com/fastapi-cli/" target="_blank">FastAPI CLI ഡോക്യുമെന്റുകളിൽ</a> ഇതിനെക്കുറിച്ച് നിങ്ങൾക്ക് കൂടുതൽ വായിക്കാം.

</details>

### Check it

<a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a> എന്ന അഡ്രസ് നിങ്ങളുടെ ബ്രൗസറിൽ  തുറക്കുക.

നിങ്ങൾക്ക് JSON പ്രതികരണം ഇങ്ങനെ കാണാനാകും:

```JSON
{"item_id": 5, "q": "somequery"}
```

നിങ്ങൾ ഇതിനകം തന്നെ ഒരു API സൃഷ്ടിച്ചിട്ടുണ്ട്, അത്:

* _paths_ `/`, `/items/{item_id}` എന്നിവയിൽ HTTP അഭ്യർത്ഥനകൾ സ്വീകരിക്കുന്നു.
* രണ്ട് _paths_ ഉം `GET` <em>പ്രവർത്തനങ്ങൾ</em> (HTTP _methods_ എന്നും അറിയപ്പെടുന്നു) എടുക്കുന്നു.
* _path_ `/items/{item_id}` ന് ഒരു `int` ആയിരിക്കണം _path parameter_ `item_id` ഉണ്ട്.
* _path_ `/items/{item_id}` ന് ഒരു ഓപ്‌ഷണൽ `str` _query പാരാമീറ്റർ_ `q` ഉണ്ട്.

### ഇൻറ്ററാക്റ്റിവ് API ഡോക്യൂമെന്റുകൾ

ഇനി <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> എന്നതിലേക്ക് പോകുക.

നിങ്ങൾക്ക് ഓട്ടോമാറ്റിക് ഇന്ററാക്ടീവ് API ഡോക്യുമെന്റേഷൻ കാണാൻ കഴിയും (<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">സ്വാഗർ UI</a> നൽകുന്നത്):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### ഇതര API ഡോക്യൂമെന്റുകൾ

ഇനി, <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> എന്നതിലേക്ക് പോകുക.

നിങ്ങൾക്ക് ഇതര ഓട്ടോമാറ്റിക് ഡോക്യുമെന്റേഷൻ കാണാൻ കഴിയും (<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> നൽകുന്നത്):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## ഉദാഹരണ നവീകരണം

ഇനി `PUT` അഭ്യർത്ഥനയിൽ നിന്ന് ഒരു ബോഡി സ്വീകരിക്കുന്നതിന് `main.py` ഫയൽ പരിഷ്കരിക്കുക.

സ്റ്റാൻഡേർഡ് പൈത്തൺ തരങ്ങൾ ഉപയോഗിച്ച് ബോഡി പ്രഖ്യാപിക്കുക, പൈഡാന്റിക്കിന് നന്ദി.

```Python hl_lines="4  9-12  25-27"
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

`fastapi dev` സെർവർ യാന്ത്രികമായി റീലോഡ് ചെയ്തിട്ടുണ്ടാവണം.

### ഇൻറ്ററാക്റ്റിവ് API ഡോക്‌സ് അപ്‌ഗ്രേഡ്

ഇനി <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> എന്നതിലേക്ക് പോകുക.

* പുതിയ ബോഡി ഉൾപ്പെടെ, ഇൻറ്ററാക്റ്റിവ് API ഡോക്യുമെന്റേഷൻ സ്വയമേവ അപ്ഡേറ്റ് ചെയ്യപ്പെടും:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

* "ഇത് പരീക്ഷിച്ചുനോക്കൂ" എന്ന ബട്ടണിൽ ക്ലിക്കുചെയ്യുക, ഇത് പാരാമീറ്ററുകൾ പൂരിപ്പിക്കാനും API-യുമായി നേരിട്ട് സംവദിക്കാനും നിങ്ങളെ അനുവദിക്കുന്നു:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

* തുടർന്ന് "എക്സിക്യൂട്ട്" ബട്ടണിൽ ക്ലിക്കു ചെയ്യുക, ഉപയോക്തൃ ഇന്റർഫേസ് നിങ്ങളുടെ API-യുമായി ആശയവിനിമയം നടത്തുകയും പാരാമീറ്ററുകൾ അയയ്ക്കുകയും ഫലങ്ങൾ നേടുകയും സ്ക്രീനിൽ കാണിക്കുകയും ചെയ്യും:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### ഇതര API ഡോക്യൂമെന്റുകൾ നവീകരണം

ഇനി, <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> എന്നതിലേക്ക് പോകുക.

* ഇതര ഡോക്യുമെന്റേഷൻ പുതിയ ക്വറി പാരാമീറ്ററും ബോഡിയും പ്രതിഫലിപ്പിക്കും:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### പുനരാവലോകനം

ചുരുക്കത്തിൽ, നിങ്ങൾ പാരാമീറ്ററുകളുടെ തരങ്ങൾ, ബോഡി മുതലായവ **ഒരിക്കൽ** ഫംഗ്ഷൻ പാരാമീറ്ററുകളായി പ്രഖ്യാപിക്കുന്നു.

സ്റ്റാൻഡേർഡ് ആധുനിക പൈത്തൺ തരങ്ങൾ ഉപയോഗിച്ചാണ് നിങ്ങൾ അത് ചെയ്യുന്നത്.

നിങ്ങൾ ഒരു പുതിയ വാക്യഘടന, ഒരു പ്രത്യേക ലൈബ്രറിയുടെ രീതികൾ അല്ലെങ്കിൽ ക്ലാസുകൾ മുതലായവ പഠിക്കേണ്ടതില്ല.

വെറും സ്റ്റാൻഡേർഡ് **പൈത്തൺ**.

ഉദാഹരണത്തിന്, ഒരു `int` ന്:

```Python
item_id: int
```

അല്ലെങ്കിൽ കൂടുതൽ സങ്കീർണ്ണമായ ഒരു `Item` മോഡലിന്:

```Python
item: Item
```

...ആ ഒരൊറ്റ പ്രസ്താവനയിലൂടെ നിങ്ങൾക്ക് ലഭിക്കുന്നത്:

* എഡിറ്റർ പിന്തുണ, ഇതിൽ ഉൾപെടുന്നവ:
    * പൂർത്തീകരണം.
    * ടൈപ്പ് പരിശോധനകൾ.
* ഡാറ്റയുടെ സാധൂകരണം:
    * ഡാറ്റ അസാധുവാകുമ്പോൾ യാന്ത്രികവും മായ്‌ക്കുന്നതുമായ പിശകുകൾ.
    * ആഴത്തിൽ നെസ്റ്റഡ് JSON ഒബ്‌ജക്‌റ്റുകൾക്കുപോലും സാധൂകരണം.
* ഇൻപുട്ട് ഡാറ്റയുടെ <abbr title="also known as: serialization, parsing, marshalling">പരിവർത്തനം</abbr>:നെറ്റ്‌വർക്കിൽ നിന്ന് പൈത്തൺ ഡാറ്റയിലേക്കും തരങ്ങളിലേക്കും വരുന്നു. ഈ കംപോണന്റുകളിൽ നിന്നു വായിക്കുന്നു :ഹെഡ്‍റുകൾ
    * JSON.
    * പാഥ് പാരാമീറ്ററുകൾ.
    * ക്വറി പാരാമീറ്ററുകൾ.
    * കുക്കീസ്‌ .
    * ഹെഡ്‍റുകൾ .
    * ഫോമുകൾ .
    * ഫയലുകൾ .
* ഔട്ട്‌പുട്ട് ഡാറ്റയുടെ <abbr title="also known as: serialization, parsing, marshalling">പരിവർത്തനം</abbr>: പൈത്തൺ ഡാറ്റയിൽ നിന്നും തരങ്ങളിൽ നിന്നും നെറ്റ്‌വർക്ക് ഡാറ്റയിലേക്ക് പരിവർത്തനം ചെയ്യുന്നു (JSON ആയി):
    * പൈത്തൺ തരങ്ങൾ പരിവർത്തനം ചെയ്യുക (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` ഒബ്ജെക്ട്സ് .
    * `UUID` ഒബ്ജെക്ട്സ് .
    * ഡാറ്റാബേസ് മോഡലുകൾ.
    * ...കൂടാതെ മറ്റു പലതും.
* രണ്ട് ഇതര ഉപയോക്തൃ ഇന്റർഫേസുകൾ ഉൾപ്പെടെ ഓട്ടോമാറ്റിക് ഇന്ററാക്ടീവ് API ഡോക്യുമെന്റേഷൻ:
    * സ്വാഗർ UI.
    * റീഡോക്.

---

മുമ്പത്തേ കോഡ് ഉദാഹരണത്തിലേക്ക് തിരികെ വരുമ്പോൾ, **ഫാസ്റ്റ് API** ഇനിപ്പറയുന്നവ ചെയ്യും:

* `GET`, `PUT` അഭ്യർത്ഥനകൾക്കുള്ള പാതയിൽ ഒരു `item_id` ഉണ്ടെന്ന് സാധൂകരിക്കുക.
* `GET`, `PUT` അഭ്യർത്ഥനകൾക്കായി `item_id` `int` തരത്തിലുള്ളതാണെന്ന് സാധൂകരിക്കുക.
    * അങ്ങനെയല്ലെങ്കിൽ, ക്ലയന്റ് ഉപയോഗപ്രദവും വ്യക്തവുമായ ഒരു പിശക് കാണും.
* `GET` അഭ്യർത്ഥനകൾക്കായി `q` (`http://127.0.0.1:8000/items/foo?q=somequery` പോലെ) എന്ന പേരിൽ ഒരു ഓപ്ഷണൽ അന്വേഷണ പാരാമീറ്റർ ഉണ്ടോ എന്ന് പരിശോധിക്കുക.
    * `q` പാരാമീറ്റർ `= None` എന്ന് പ്രഖ്യാപിച്ചിരിക്കുന്നതിനാൽ, അത് ഓപ്ഷണലാണ്.
    * `None` ഇല്ലെങ്കിൽ അത് ആവശ്യമായി വരും (`PUT` ലെ ബോഡി പോലെ).
* `/items/{item_id}` ലേക്കുള്ള `PUT` അഭ്യർത്ഥനകൾക്ക്, ബോഡി JSON ആയി വായിക്കുക:
    * അതിന് ഒരു `str` ആയിരിക്കേണ്ട ഒരു ആവശ്യമായ ആട്രിബ്യൂട്ട് `name` ഉണ്ടോയെന്ന് പരിശോധിക്കുക.
    * അതിന് `price` എന്ന ഒരു required ആട്രിബ്യൂട്ട് ഉണ്ടോ എന്നും അത് ഒരു `float` ആയിരിക്കണമെന്നും പരിശോധിക്കുക.
    * ഇതിന് `is_offer` എന്ന ഓപ്‌ഷണൽ ആട്രിബ്യൂട്ട് ഉണ്ടോയെന്ന് പരിശോധിക്കുക, ഉണ്ടെങ്കിൽ അത് `bool` ആയിരിക്കണം.
    * ഇതെല്ലാം ഡീപ്ലി  നെസ്റ്റഡ് JSON ഒബ്‌ജക്‌റ്റുകൾക്കും പ്രവർത്തിക്കും.
* JSON-ൽ നിന്നും JSON-ലേയ്ക്കും സ്വയമേവ പരിവർത്തനം ചെയ്യുക.
* OpenAPI ഉപയോഗിച്ച് എല്ലാം രേഖപ്പെടുത്തുക, അത് ഇനിപ്പറയുന്നവർക്ക് ഉപയോഗിക്കാം:
    * ഇന്ററാക്ടീവ് ഡോക്യുമെന്റേഷൻ സിസ്റ്റങ്ങൾ.
    * പല ഭാഷകൾക്കുമായി ഓട്ടോമാറ്റിക് ക്ലയന്റ് കോഡ് ജനറേഷൻ സിസ്റ്റങ്ങൾ.
* 2 ഇന്ററാക്ടീവ് ഡോക്യുമെന്റേഷൻ വെബ് ഇന്റർഫേസുകൾ നേരിട്ട് നൽകുക.

---

ഞങ്ങൾ ഉപരിതലം മുഴുവൻ വായിച്ചു, പക്ഷേ ഇതെല്ലാം എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്നതിന്റെ ഒരു ധാരണ നിങ്ങൾക്ക് ഇതിനകം ലഭിച്ചുകഴിഞ്ഞു.

ഇതുപയോഗിച്ച് ലൈൻ മാറ്റാൻ ശ്രമിക്കുക:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...from:

```Python
        ... "item_name": item.name ...
```

...to:

```Python
        ... "item_price": item.price ...
```

...നിങ്ങളുടെ എഡിറ്റർ ആട്രിബ്യൂട്ടുകൾ എങ്ങനെ യാന്ത്രികമായി പൂർത്തിയാക്കുമെന്നും അവയുടെ തരങ്ങൾ എങ്ങനെ അറിയുമെന്നും കാണുക:

![എഡിറ്റർ പിന്തുണ](https://fastapi.tiangolo.com/img/vscode-completion.png)

കൂടുതൽ സവിശേഷതകൾ ഉൾപ്പെടെയുള്ള കൂടുതൽ പൂർണ്ണമായ ഉദാഹരണത്തിന്, <a href="https://fastapi.tiangolo.com/tutorial/">ട്യൂട്ടോറിയൽ - ഉപയോക്തൃ ഗൈഡ്</a> കാണുക.

**സ്‌പോയിലർ അലേർട്ട്**: ട്യൂട്ടോറിയൽ - ഉപയോക്തൃ ഗൈഡിൽ ഇവ ഉൾപ്പെടുന്നു:

* മറ്റ് വ്യത്യസ്ത സ്ഥലങ്ങളിൽ നിന്നുള്ള **പാരാമീറ്ററുകളുടെ** പ്രഖ്യാപനം: **ഹെഡറുകൾ**, **കുക്കികൾ**, **ഫോം ഫീൽഡുകൾ**, **ഫയലുകൾ**.
* **മൂല്യനിർണ്ണയ നിയന്ത്രണങ്ങൾ** `maximum_length` അല്ലെങ്കിൽ `regex` ആയി എങ്ങനെ സജ്ജമാക്കാം.
* വളരെ ശക്തവും ഉപയോഗിക്കാൻ എളുപ്പമുള്ളതുമായ ഒരു **<abbr title="components, resources, providers, services, injectables">ഡിപ്പെൻഡൻസി ഇഞ്ചക്ഷൻ</abbr>** സിസ്റ്റം.
* സുരക്ഷയും ഓതെന്റിക്കേഷനും , **JWT ടോക്കണുകൾ** ഉള്ള **OAuth2** നുള്ള പിന്തുണയും **HTTP ബേസിക്** ഓത്തും ഉൾപ്പെടെ.
* **ഡീപ്ലി നെസ്റ്റഡ് JSON മോഡലുകൾ** പ്രഖ്യാപിക്കുന്നതിനുള്ള കൂടുതൽ വിപുലമായ (എന്നാൽ അത്രതന്നെ എളുപ്പമുള്ള) സാങ്കേതിക വിദ്യകൾ (പൈഡന്റിക്കിന് നന്ദി).
* **ഗ്രാഫ് QL** <a href="https://strawberry.rocks" class="external-link" target="_blank">സ്ട്രോബെറി</a>, മറ്റ് ലൈബ്രറികൾ എന്നിവയുമായുള്ള സംയോജനം.
* നിരവധി അധിക സവിശേഷതകൾ (സ്റ്റാർലെറ്റിന് നന്ദി) ഇവയാണ്:
    * **വെബ്‌സോക്കറ്റുകൾ**
    * HTTPX, `pytest` എന്നിവ അടിസ്ഥാനമാക്കിയുള്ള വളരെ എളുപ്പമുള്ള പരിശോധനകൾ
    * **CORS**
    **കുക്കി സെഷനുകൾ**
    * ...പിന്നെ മറ്റുപലതും.

## പ്രകടനം

സ്വതന്ത്ര TechEmpower ബെഞ്ച്മാർക്കുകൾ, യൂവികോൺ -ന് കീഴിൽ പ്രവർത്തിക്കുന്ന **ഫാസ്റ്റ്API** ആപ്ലിക്കേഷനുകൾ <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">ലഭ്യമായ ഏറ്റവും വേഗതയേറിയ പൈത്തൺ ഫ്രെയിംവർക്കുകളിൽ ഒന്നായി</a> കാണിക്കുന്നു, ഇത് സ്റ്റാർലെറ്റ് , യൂവികോൺ  എന്നിവയ്ക്ക് താഴെയാണ് (ഫാസ്റ്റ്API ആന്തരികമായി ഉപയോഗിക്കുന്നു). (*)

ഇതിനെക്കുറിച്ച് കൂടുതലറിയാൻ, <a href="https://fastapi.tiangolo.com/benchmarks/" class="internal-link" target="_blank">ബെഞ്ച്മാർക്സ്</a> എന്ന വിഭാഗം കാണുക.

## ആശ്രിതത്വങ്ങൾ

ഫാസ്റ്റ്API പൈഡാന്റിക്, സ്റ്റാർലെറ്റ് എന്നിവയെ ആശ്രയിച്ചിരിക്കുന്നു.

### `സ്റ്റാൻഡേർഡ്` ആശ്രിതത്വങ്ങൾ

`pip install "fastapi[standard]"` ഉപയോഗിച്ച് ഫാസ്റ്റ് API ഇൻസ്റ്റാൾ ചെയ്യുമ്പോൾ അത് ഓപ്ഷണൽ ഡിപൻഡൻസികളുടെ `standard` ഗ്രൂപ്പുമായി വരുന്നു:

പൈഡാന്റിക് ഉപയോഗിക്കുന്നത്:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>ഇ-മെയിൽ-വാലിഡേറ്റർ</code></a> - ഇ-മെയിൽ വാലിഡേഷനായി.

സ്റ്റാർലെറ്റ് ഉപയോഗിച്ചത്:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - `TestClient` ഉപയോഗിക്കണമെങ്കിൽ ആവശ്യമാണ്.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - ഡിഫോൾട്ട് ടെംപ്ലേറ്റ് കോൺഫിഗറേഷൻ ഉപയോഗിക്കണമെങ്കിൽ ആവശ്യമാണ്.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - `request.form()` ഉപയോഗിച്ച് <abbr title="ഒരു HTTP അഭ്യർത്ഥനയിൽ നിന്ന് വരുന്ന സ്ട്രിംഗിനെ പൈത്തൺ ഡാറ്റയിലേക്ക് പരിവർത്തനം ചെയ്യൽ">"പാഴ്‌സിംഗ്"</abbr> എന്ന ഫോമിനെ പിന്തുണയ്ക്കണമെങ്കിൽ ആവശ്യമാണ്.

ഫാസ്റ്റ് API / സ്റ്റാർലെറ്റ് ഉപയോഗിക്കുന്നത്:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - നിങ്ങളുടെ ആപ്ലിക്കേഷൻ ലോഡ് ചെയ്ത് സെർവ് ചെയ്യുന്ന സെർവറിനുള്ളത്. ഇതിൽ `uvicorn[standard]` ഉൾപ്പെടുന്നു, ഉയർന്ന പ്രകടനമുള്ള സെർവിംഗിന് ആവശ്യമായ ചില ആശ്രിതത്വങ്ങൾ (ഉദാ. `uvloop`) ഇതിൽ ഉൾപ്പെടുന്നു.
* `fastapi-cli` - `fastapi` കമാൻഡ് നൽകാൻ.

### `സ്റ്റാൻഡേർഡ്` ആശ്രിതത്വങ്ങൾ ഇല്ലാതെ

`സ്റ്റാൻഡേർഡ്` ഓപ്ഷണൽ ആശ്രിതത്വങ്ങൾ ഉൾപ്പെടുത്താൻ നിങ്ങൾ ആഗ്രഹിക്കുന്നില്ലെങ്കിൽ, `pip install "fastapi[standard]"` എന്നതിന് പകരം `pip install fastapi` ഉപയോഗിച്ച് ഇൻസ്റ്റാൾ ചെയ്യാം.

### അധിക ഓപ്ഷണൽ ആശ്രിതത്വങ്ങൾ

നിങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യാൻ ആഗ്രഹിക്കുന്ന ചില അധിക ആശ്രിതത്വങ്ങൾ.

അധിക ഓപ്ഷണൽ പൈഡാന്റിക് ആശ്രിതത്വങ്ങൾ:

* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> - ക്രമീകരണ മാനേജ്മെന്റിനായി.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> - പൈഡന്റിക്കിനൊപ്പം ഉപയോഗിക്കേണ്ട എക്സ്ട്രാ തരങ്ങൾക്കായി.

അധിക ഓപ്ഷണൽ ഫാസ്റ്റ് API ആശ്രിതത്വങ്ങൾ:

* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - `ORJSONResponse` ഉപയോഗിക്കണമെങ്കിൽ ആവശ്യമാണ്.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - `UJSONResponse` ഉപയോഗിക്കണമെങ്കിൽ ആവശ്യമാണ്.

## ലൈസൻസ്

ഈ പ്രോജക്റ്റ് MIT ലൈസൻസിന്റെ നിബന്ധനകൾക്ക് കീഴിലാണ് ലൈസൻസ് ചെയ്തിരിക്കുന്നത്.
