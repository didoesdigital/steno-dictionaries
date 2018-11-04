# Steno Dictionaries

This repository contains Di’s stenography dictionaries used by [Typey Type for Stenographers](https://didoesdigital.com/typey-type/). The dictionaries are in JSON format and use [Plover](http://stenoknight.com/wiki/FAQ#What_is_Plover.3F) theory.

[Typey Type’s dictionary](https://didoesdigital.com/typey-type/dictionaries/typey-type/typey-type/) is generated from this subset of this repo’s dictionaries:

- `abbreviations.json`
- `briefs.json`
- `condensed-strokes.json`
- `currency.json`
- `dict.json`
- `dict-en-AU-phonetic.json`
- `dict-en-AU-vocab.json`
- `dict-en-AU-with-extra-stroke.json`
- `nouns.json`
- `numbers.json`
- `numbers-powerups.json`
- `pronouns.json`
- `punctuation-di.json`
- `punctuation-powerups.json`
- `punctuation-unspaced.json`
- `symbols.json`
- `symbols-briefs.json`
- `symbols-currency.json`
- `top-10000-english-words.json`
- `top-10000-project-gutenberg-words.json`
- `top-level-domains.json`

The majority of Typey Type’s dictionary is from `dict.json`. It follows [Plover's default `main.json` dictionary](https://github.com/openstenoproject/plover/blob/master/plover/assets/main.json) with misstrokes removed from the top 10,000 words. You can use this dictionary instead of Plover’s.

**The aim is to remove all the misstrokes from `dict.json` to give new stenographers greater confidence in learning new briefs.** The first step is to remove all the misstrokes for the *shortest* available brief for every word. If there’s a misstroke in a longer word, it is less likely to be suggested by Typey Type or dictionary look up tools.

If you notice any misstrokes, see the Contributing guide below.



# Dictionaries

Here are all the dictionaries included:

* [abbreviations.json](dictionaries/abbreviations.json)
* [apps.json](dictionaries/apps.json)
* [bad-habits.json](dictionaries/bad-habits.json)
* [briefs.json](dictionaries/briefs.json)
* [code.json](dictionaries/code.json)
* [computer-powerups.json](dictionaries/computer-powerups.json)
* [computer-use.json](dictionaries/computer-use.json)
* [css-alignment.json](dictionaries/css-alignment.json)
* [css-declarations.json](dictionaries/css-declarations.json)
* [css-media-object.json](dictionaries/css-media-object.json)
* [condensed-strokes.json](dictionaries/condensed-strokes.json)
* [currency.json](dictionaries/currency.json)
* [di-spectacle-v1.json](dictionaries/di-spectacle-v1.json)
* [dict-en-AU-phonetic.json](dictionaries/dict-en-AU-phonetic.json)
* [dict-en-AU-vocab.json](dictionaries/dict-en-AU-vocab.json)
* [dict-en-AU-with-extra-stroke.json](dictionaries/dict-en-AU-with-extra-stroke.json)
* [dict.json](dictionaries/dict.json)
* [emoji.json](dictionaries/emoji.json)
* [fingerspelling-FPLT.json](dictionaries/fingerspelling-FPLT.json)
* [fingerspelling-powerups.json](dictionaries/fingerspelling-powerups.json)
* [fingerspelling-RBGS.json](dictionaries/fingerspelling-RBGS.json)
* [fingerspelling-right-hand.json](dictionaries/fingerspelling-right-hand.json)
* [git.json](dictionaries/git.json)
* [html.json](dictionaries/html.json)
* [javascript.json](dictionaries/javascript.json)
* [lorem.json](dictionaries/lorem.json)
* [markdown.json](dictionaries/markdown.json)
* [medical-suffixes.json](dictionaries/medical-suffixes.json)
* [modifiers-single-stroke.json](dictionaries/modifiers-single-stroke.json)
* [modifiers.json](dictionaries/modifiers.json)
* [navigation.json](dictionaries/navigation.json)
* [nouns.json](dictionaries/nouns.json)
* [numbers-powerups.json](dictionaries/numbers-powerups.json)
* [numbers.json](dictionaries/numbers.json)
* [plover-powerups.json](dictionaries/plover-powerups.json)
* [plover-use.json](dictionaries/plover-use.json)
* [pronouns.json](dictionaries/pronouns.json)
* [punctuation-di.json](dictionaries/punctuation-di.json)
* [punctuation-powerups.json](dictionaries/punctuation-powerups.json)
* [punctuation-unspaced.json](dictionaries/punctuation-unspaced.json)
* [punctuation.json](dictionaries/punctuation.json)
* [python.json](dictionaries/python.json)
* [ruby.json](dictionaries/ruby.json)
* [shortcuts.json](dictionaries/shortcuts.json)
* [sketch-app.json](dictionaries/sketch-app.json)
* [sublime.json](dictionaries/sublime.json)
* [symbol-briefs.json](dictionaries/symbol-briefs.json)
* [symbol-currency.json](dictionaries/symbol-currency.json)
* [symbol-currency-culled.json](dictionaries/symbol-currency-culled.json)
* [symbols.json](dictionaries/symbols.json)
* [tabbing.json](dictionaries/tabbing.json)
* [top-100-words.json](dictionaries/top-100-words.json)
* [top-1000-words.json](dictionaries/top-1000-words.json)
* [top-10000-project-gutenberg-words.json](dictionaries/top-10000-project-gutenberg-words.json)
* [top-10000-english-words.json](dictionaries/top-10000-english-words.json)
* [top-level-domains.json](dictionaries/top-level-domains.json)
* [ux-design.json](dictionaries/ux-design.json)
* [vim.json](dictionaries/vim.json)
* [voiceover.json](dictionaries/voiceover.json)



## English Dictionaries

- A main [`dict.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/dict.json) dictionary, containing many English words using briefs and phonetic strokes, but contains fewer misstrokes.
- A [`top-10000-project-gutenberg-words.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/top-10000-project-gutenberg-words.json) dictionary, containing 10,000 common words from [Project Gutenberg](https://www.gutenberg.org/). This is a great starter dictionary.
- A [`google-10000-english.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/google-10000-english.json) dictionary, including 10,000 popular English words by N-grams; credit goes to [Josh Kaufman's typing word list from Google's Trillion Word Corpus](https://github.com/first20hours/google-10000-english).



## Plover dictionaries

The main [plover-use.json](dictionaries/plover-use.json) helps you use the Plover app itself as well as managing spacing and casing in Plover:

- `"TPHR*URB": "{}",`: [Cancels formatting of next word](https://github.com/openstenoproject/plover/wiki/Dictionary-Format#canceling-formatting-of-next-word)
- `"#: {*+}`: repeats the previous stroke
- `"#*: {*}`: toggles the asterisk key on the previous stroke
- `"S-P: {^ ^}`: produces a space
- `"KPA: {-|}`: forces the first letter of the next word to be uppercase
- `"HRO*ER: {&gt;}`: forces the first letter of the next word to be lowercase
- ~~`"{^ ^}`: inserts space without affecting case~~
- ~~`"{^}`: suppresses a space without affecting case~~
- `"TK*LS: {^^}`: removes a space without affecting case
- `"KPA*Z: {*-|}`: retrospectively capitalise/uppercase first letter
- `"KPA*EUZ: {*&gt;}`: retrospectively lowercase first letter
- `"KPA*EZ: {*&lt;}`: retrospectively uppercase all letters
- `"AFPS: {*?}`: retrospectively inserts a space
- `"TK-FPS: {*!}`: retrospectively remove space
- `"KPA*E: {&lt;}`: forces the next letter to be uppercase
- `"KPA*EU: {^}{&lt;}`: suppresses a space and forces the next letter to be uppercase
- `"KPA*L: {&lt;}`: uppercases the next word
- `"KW-GS: {~|\"^}`: carries the capital letter across the next quotation mark
- `"KR-GS: {^~|\"}`: carries the capital letter across the next quotation mark
- `"PREPB: {~|(^}`: carries the capital letter across the next parenthesis
- `"PR*EPB: {^~|)}`: carries the capital letter across the next parenthesis
- `"HRO*ER: {MODE:LOWER}`: switches to lowercase mode so all letters are lowercase
- `"K-BGS: {MODE:CAMEL}`: switches to camelCase mode so spaces are suppressed and subsequent words are capitalised
- `"KA*PS: {MODE:CAPS}`: switches to all caps or uppercase mode so all letters are uppercase
- `"KHRAO*ER: {MODE:CLEAR}`: clears all mode settings
- `"KPHA*PLD: {MODE:SET_SPACE:, }`: sets a custom space mode that replaces all spaces with spaces (normal spacing—you can swap the space character for any character)
- `"SPAO*EUPBL: {MODE:LOWER} {MODE:SET_SPACE:-}`: switches to lowercase mode and sets the spaces to hyphens for a kind of “spinal case”
- `"STPHA*EUBG: {MODE:SNAKE}`: switches to snake case mode so all spaces are replaces with underscores
- `"TAO*EULT: {MODE:TITLE}`: switches to title case mode so each word is capitalised
- `"TPHO*EFP: {MODE:SET_SPACE:}`: sets to a custom space mode that replaces all spaces with nothing, suppressing spaces
- `"R*EFT: {MODE:RESET}`: resets all case and spacing modes
- `"R*EFTZ: {MODE:RESET_CASE}`: resets case modes
- `"R*EFTZ: {MODE:RESET_SPACE}`: resets spacing modes
- `"TKUPT": "{PLOVER:ADD_TRANSLATION}",`: opens Plover’s add translation window
- `"PHRAOBG": "{PLOVER:LOOKUP}",`: opens Plover’s add translation window
- `"PHREUG": "{PLOVER:CONFIGURE}",`: opens Plover’s configuration
- `"PHREUT/PHREUT": "{PLOVER:QUIT}",`: quits Plover’s
- `"PHROEUBGS": "{PLOVER:FOCUS}",`: brings Plover to the front (window focus)
- `"PHROF": "{PLOVER:SUSPEND}",`: disables Plover’s steno behaviour
- `"PHROLG": "{PLOVER:TOGGLE}",`: toggles Plover’s steno behaviour between on and off
- `"PHROPB": "{PLOVER:RESUME}",`: enables Plover’s steno behaviour



## Vocabulary Dictionaries

- [`nouns.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/nouns.json) contains a few hundred additional words.
- [`pronouns.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/pronouns.json) contains a few hundred pronouns.
- [`condensed-strokes.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/condensed-strokes.json) contains a combinations of existing strokes in the main Plover dictionary so that they appear in searches when you look up strokes. These words can already be written using the default Plover dictionary and prefix/suffix strokes or punctuation strokes. It can be useful for improving dictionary lookups, but is not needed to write the words.



## Fingerspelling Dictionaries

Based on [Plover's default `main.json` dictionary](https://github.com/openstenoproject/plover/blob/master/plover/assets/main.json), this repo contains 2 alternative fingerspelling dictionaries:

- A [`fingerspelling-FPLT.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/fingerspelling-FPLT.json) dictionary, using fingerspelled letters on the left hand and `-FPLT` on the right hand.
- A [`fingerspelling-RBGS.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/fingerspelling-RBGS.json) dictionary, using fingerspelled letters on the left hand and `-RBGS` on the right hand.



## Navigation and Tabbing Dictionaries

This dictionary lets you navigate and edit text efficiently on a Mac. You can move the cursor by letter, word, or line, select while doing so, and also backspace or forward delete by character, word, or line.

To use the following briefs, copy the [`navigation.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/navigation.json) file into your dictionary folder and add it to your Plover config:

As per Plover's default, you use `-R`, `-P`, `-B`, and `-G` for left, up, down, and right.

Use `STPH-` to move by character, `STPH-RB` to jump a word left, and `STPH-BG` to jump a word right.

Use `KPH-` to use Command ⌘, jumping to line beginning and ending, file top and bottom.

Use `STP-` (**s**hi**f**t) to select characters with movement keys. Again, `-RB` and `-BG` work by word.

Use `SHR-` (**s**e**l**ect) to select words with the movement keys. (This and the strokes described above actually add redundant strokes for selecting whole words to the left and right.)

Use `PW*` and `-F`, `-FP`, or `-FPL` for backspacing a character, a word, or a line.

Use `PW*` and `-R`, `-RB`, or `-RBG` for forward deleting a character, a word, or a line.

Use `KPHR-` for Command + Option (⌘⌥) movements (usually for navigating tabs and file trees).

Use `SP-B` to space up/forward and `SP-P` to space down/backward. That is, in the browser use the former stroke to page up and the latter to page down (this is using ⇧Space).

Use `THRAB` for ⌥ ⇓ and `THRAP` for ⌥ ⇑.

The complementary [`tabbing.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/navigation.json) dictionary also lets you switch tabs, windows, and apps.

Use `TW-` and a direction for tabbing. Adding `-F`/`-L` gives you ⌘⇧[/⌘⇧] to switch tabs forward and backward. Adding `-B`/`-G` gives you ⌘\`/⌘⇧\` to switch windows forward and backward. Adding `-G`/`-R` gives you ⌘Tab/⌘⇧Tab to switch applications forward and backward. Adding `-FB`/`-LG` gives you ⌘[/⌘] to navigate forwards and backwards in a browser. Adding a star to `TW*G` gives you ⌘Tab Tab to switch 2 applications.



## Computer Powerups Dictionary

This dictionary was designed for running commands on a Mac. Copy the [`computer-powerups.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/computer-powerups.json) file into your dictionary folder and add it to your Plover config to use the following briefs:

* Tab and Space keys `"STA*PB": "{#Tab}{#space}",`
* Mac Character Viewer `"KHA*RZ": "{#Control_L(Super_L(space))}",`
* Shift Return key (⇧↵) `"STP*R": "{#Shift_L(Return)}",`
* Command backslash (⌘/) `"O*EURPLT": "{#Super_L(backslash)}",`
* Command Shift backslash (⌘⇧/) `"O*EURPBLT": "{#Super_L(Shift_L(backslash))}",`
* Audio play `"PHRA*EU": "{#AudioPlay}",`
* Audio raise volume `"SROPL": "{#AudioRaiseVolume}",`
* Audio lower volume `"SRO*PL": "{#AudioLowerVolume}",`
* Audio next `"TPH*EGT": "{#AudioNext}",`
* Audio mute `"PHAO*UT": "{#AudioMute}",`
* Monitor brightness up `"PWROEUT": "{#MonBrightnessUp}",`
* Monitor brightness down `"PWRO*EUT": "{#MonBrightnessDown}",`
* Keyboard brightness up `"KPWROEUT": "{#KbdBrightnessDown}",`
* Keyboard brightness down `"KPWRO*EUT": "{#KbdBrightnessUp}",`
* Command Escape `"KPH*/TPEFBG": "{#Super_L(Escape)}",`
* Command Space `"-FRL": "{#Super_L(space)} {^}",`
* Command Space (alternative) `"A*FRL": "{#Super_L(space)} {^}",`
* Command Option C (⌘⌥C) to copy from clipboard history `"KPWR*": "{#command(option(c))}",`
* Command Return `"KPHR*R": "{#command(return)}",`
* Control Space `"SP-LT": "{#Control_L(space)}{^}",`
* Option Escape for Speak selected text `"SPAO*EBG": "{#Alt_L(Escape)}",`
* Screenshot selected area as a file `"SKR*PB": "{#Super_L(Shift_L(4))}",`
* Screenshot selected area and copy to clipboard `"SKR*RPB": "{#Super_L(Control_L(Shift_L(4)))}",`



## Punctuation Dictionary

Copy the [`punctuation.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/punctuation.json) file into your dictionary folder and add it to your Plover config to use the following briefs:

* . `TP-PL` =&gt; `F-PL` (<strong>f</strong>u<strong>ll</strong> sto<strong>p</strong>, spaced)
* . `P-P` (decimal <strong>p</strong>oint, unspaced)
* ... `SKWR-RBGS` =&gt; `SY-SHUN` (<strong>su</strong>spen<strong>sion</strong> point, then capital)
* ... `HR-PS` =&gt; `L-PS` (e<strong>ll</strong>i<strong>ps</strong>is, then lowercase)
* ? `H-F` (question mark, spaced)
* ! `SKHRAPL` =&gt; `SKLAM` (e<strong>xclam</strong>ation mark, spaced)
* ' `A*E` (opening single quote/<strong>a</strong>postroph<strong>e</strong>, no space)
* ' `AE` (closing single quote/<strong>a</strong>postroph<strong>e</strong>, space)
* " `KW-GS` =&gt; `Q-SHUN` (opening <strong>q</strong>uota<strong>tion</strong> mark, no space)
* " `KR-GS` =&gt; `C-SHUN` (<strong>c</strong>losing quota<strong>tion</strong> mark, space)
* , `KW-BG` (comma, spaced)
* ; `SKWR*RBGS` or `STPH*FPLT` (semi-colon, spaced)
* : `STPH-FPLT` (colon, spaced)
* : `KHR-PB` =&gt; `KL-N` (<strong>c</strong>o<strong>l</strong>o<strong>n</strong>, unspaced)
* - `H-PB` =&gt; `H-PB` (<strong>h</strong>yphe<strong>n</strong>), unspaced
* -- `TK-RB` =&gt; `D-SH` (<strong>d</strong>a<strong>sh</strong>)
* - `PH*PBS` =&gt; `M-NS` (<strong>m</strong>i<strong>n</strong>u<strong>s</strong>, spaced)
* + `PHR*US` => `PL*US` (<strong>plus</strong>)
* = `KWA*LS` =&gt; `QA*LS` (unspaced e<strong>q</strong>u<strong>als</strong>)
* = `KW-L` =&gt; `Q-L` (spaced e<strong>q</strong>ua<strong>l</strong>s)
* * `STA*R` (<strong>star</strong>)
* &lt; `AEPBGT` or `AEPBG` =&gt; `ANGT` (opening <strong>ang</strong>le bracke<strong>t</strong>)
* &gt; `A*EPBGT` or `A*EPBG` =&gt; `A*NGT` (closing <strong>ang</strong>le bracke<strong>t</strong>)
* &lt; `HR*PB` =&gt; `L*N` (<strong>l</strong>ess tha<strong>n</strong>)
* &gt; `TKPWR*PB` =&gt; `GR*N` (<strong>gr</strong>eater tha<strong>n</strong>)
* &lt; `PWRABG` =&gt; `BRAK` (opening angle <strong>bra</strong>c<strong>k</strong>et)
* &gt; `PWRA*BG` =&gt; `BRA*K` (closing angle <strong>bra</strong>c<strong>k</strong>et)
* ( `PREPB` =&gt; `PREN` (opening <strong>p</strong>a<strong>ren</strong>thesis)
* ) `PR*EPB` =&gt; `PR*EN` (closing <strong>p</strong>a<strong>ren</strong>thesis)
* [ `PWR-BGT` =&gt; `BR-KT` (opening <strong>br</strong>ac<strong>k</strong>e<strong>t</strong>)
* ] `PWR*BGT` =&gt; `BR*KT` (closing <strong>br</strong>ac<strong>k</strong>e<strong>t</strong>)
* { `TPR-BGT` =&gt; `FR-KT` (opening <strong>Fr</strong>ench brac<strong>k</strong>e<strong>t</strong>)
* } `TPR*BGT` =&gt; `FR*KT` (closing <strong>Fr</strong>ench brac<strong>k</strong>e<strong>t</strong>)
* / `OEU` (forward slash, unspaced)
* \ `SPWHRAERB` =&gt; `SBLAESH` (<strong>b</strong>ack<strong>slash</strong>)
* ~ `T*LD` (<strong>t</strong>i<strong>ld</strong>e, spaced)
* ~ `T*EULD` (<strong>t</strong>i<strong>ld</strong>e, unspaced)
* @ `KWRAT` =&gt; `YAT` (<strong>at</strong>-sign
* `#` `HAERB` =&gt; `HAESH` (<strong>hash</strong>)
* $ `TK-PL` =&gt; `D-M` (<strong>d</strong>ollar <strong>m</strong>ark)
* % `PERS` (<strong>perce</strong>nt)
* ^ `KR-RT` =&gt; `C-RT` (<strong>c</strong>a<strong>r</strong>e<strong>t</strong>)
* &amp; `SP-PBD` =&gt; `SP-ND` (am<strong>p</strong>er<strong>sand</strong>)
* _ `R*UPBD` or `RUPBD` =&gt; `RUND` (<strong>und</strong>e<strong>r</strong>score)
* | `PAO*EUP` (<strong>pipe</strong>)
* \` `KH-FG` =&gt; `CH-VG` (<strong>g</strong>ra<strong>v</strong>e <strong>ch</strong>aracter, backwards)
* \` `TR-RL` =&gt; `CH-VG` (opening backquote, grave brief inverted)
* \` `TR*RL` =&gt; `CH-VG` (closing backquote, grave brief inverted)
* <strong>R</strong>eturn key `R-R`
* New paragraph `SKWRAURBGS`
* Undo stroke `*`
* <strong>B</strong>ack<strong>sp</strong>ace `PW-FP` =&gt; `B-SP`
* <strong>D</strong>e<strong>l</strong>ete <strong>s</strong>pace `TK-LS` =&gt; `D-LS`
* Insert <strong>sp</strong>ace `S-P`
* <strong>Cap</strong>ital with a space `KPA`
* <strong>Cap</strong>ital without a space `KPA*`



### Punctuation Powerups Dictionary

- [`punctuation-powerups.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/punctuation-powerups.json) contains additional punctuation briefs such as:
    - pairs of punctuation (`"PWRABGS": "{^}<>{#Left}{^}"`),
    - smart/curly quotation marks (`"TP-L/TP-L": "{^’}"`), and
    - punctuation that carries capitalisation  (`"KW-GS": "{~|“^}"`).



## Unspaced Punctuation Dictionary

This dictionary uses common briefs for punctuation, but with translations that suppress surrounding spaces (before and after the punctuation) for more precise input. This might be handy for programming, for example.

To use the following briefs, copy the [`unspaced-punctuation.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/unspaced-punctuation.json) file into your dictionary folder and add it to your Plover config:

* `EPB/TKA*RB`: –
* `EPL/TKA*RB`: —
* `KH-FG`: \`
* `KR-RT`: ^
* `KA*RT`: ^
* `T*LD`: ~
* `T*EULD`: ~
* `AEPBGT`: <
* `AEPBG`: <
* `A*EPBGT`: >
* `A*EPBG`: >
* `HR*PB`: <
* `TKPWR*PB`: >
* `PWRABG`: <
* `PWRA*BG`: >
* `KWA*LS`: =
* `KW-L`: =
* `KW-LS`: ==
* `KW*LS`: ===
* `PAO*EUP`: \|
* `R*UPB`: _
* `R*UPBD`: _
* `RUPBD`: _
* `H-PB`: -
* `PH*PBS`: -
* `TK-RB`: --
* `OEU`: /
* `SPWHRAERB`: \
* `P-P`: .
* `HR-PS`: ...
* `A*E`: '
* `AE`: '
* `KW-GS`: "
* `KR-GS`: "
* `PREPB`: (
* `PR*EPB`: )
* `PWR*BGT`: ]
* `PWR-BGT`: [
* `TPR-BGT`: {
* `TPR*BGT`: }
* `TK-PL`: $
* `STA*R`: *
* `SP-PBD`: &
* `HAERB`: #
* `PERS`: %
* `PHR*US`: +

There is an additional stroke for an unspaced double quotation mark combining the opening and closing double quotation mark briefs:

* `KWR-GS`: "

You might then remove the usual strokes for opening and closing double quotation marks from your dictionary so you can still use these marks with spacing on demand. You might also replace these entries with smart or curly double quotation marks, for example:

```
"KW-GS": "{“^}",
"KR-GS": "{^”}",
```

You could then write `Test “test” test.` using `KPA* TEFT KW-GS TEFT KR-GS TEFT TP-PL`.

Similarly with single quotation marks (not included in this dictionary):

```
"TP-P": "{‘^}",
"TP-L": "{^’}",
```



## Symbols Dictionaries

- [`symbols.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/symbols.json) contains common symbols, such as degrees (`"SPWO*L/TKEGS": "°"`) and trademark (`"SPWO*L/TRAEUD/PHARBG": "{^}™"`). All of the entries are prefixed with a “symbol” stroke, `"SPWO*L": "{#}"`. The remainder of each entry’s stroke uses the stroke that would write the word instead of the symbol (for example, `"TRAEUD/PHARBG": "trademark",` and `"TKEGS": "degrees"`).
- [`symbols-briefs.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/symbols-briefs.json) contains briefs for symbols, such as `"TK*EGS": "°"`.
- [`symbols-currency.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/symbols-currency.json) contains briefs for currency symbols, such as cent (`"SPWO*L/KREPBT": "¢"`) and dollar (`"SPWO*L/TKHRAR": "$"`). All of the entries are prefixed with a “symbol” stroke, `"SPWO*L": "{#}"`. The remainder of each entry’s stroke uses the stroke that would write the word instead of the symbol (for example, `"KREPBT": "cent"` and `"TKHRAR": "dollar"`).
- [`symbols-currency-culled.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/symbols-currency-culled.json) contains only these currency symbols:

```json
"SPWO*L/KREPBT": "¢",
"SPWO*L/TKHRAR": "$",
"SPWO*L/*EUR": "€",
"SPWO*L/POUPBD/STERLG": "£",
"SPWO*L/KWREPB": "¥"
```



## Currency Dictionaries

[`currency.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/currency.json) contains briefs for currency words, such as AUD (`"*AUD": "AUD",`) and dollar (`"SWEUS/TPRAEPBG": "Swiss franc",`), a currency formatting stroke (`"K*RPBS": "{*($c)}",` so you can stroke `34/P-P/5/K*RPBS` to write $34.50), as well as briefs:

* `"TKHRAR": "dollar",`
* `"TKHRARS": "dollars",`
* `"PH-LD": "million dollar",`
* `"PH-LDZ": "million dollars",`
* `"PW-LD": "billion dollar",`
* `"PW-LDZ": "billion dollars",`
* `"TR-LD": "trillion dollar",`
* `"TR-LDZ": "trillion dollars",`

You might also like the related symbols currency dictionary:

- [`symbols-currency.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/symbols-currency.json) contains briefs for currency symbols, such as cent (`"SPWO*L/KREPBT": "¢"`) and dollar (`"SPWO*L/TKHRAR": "$"`). All of the entries are prefixed with a “symbol” stroke, `"SPWO*L": "{#}"`. The remainder of each entry’s stroke uses the stroke that would write the word instead of the symbol (for example, `"KREPBT": "cent"` and `"TKHRAR": "dollar"`).



## Australian English Dictionaries

There are two Australian English companion dictionaries, each intended to be used in combination with the default Plover dictionary. You probably only need to use ONE of these.

One overrides the default briefs with Australian variations, and also includes Australian prefixes, suffixes, alternative spellings, and vocabulary.  To use this dictionary, copy the [`dict-en-AU.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/dict-en-AU.json) file into your dictionary folder and add it to your Plover config after the default Plover dictionary so that it overrides default Plover briefs.

The other dictionary, [`dict-en-AU-with-extra-stroke.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/dict-en-AU-with-extra-stroke.json), uses a kind of suffix stroke, `/A*U`, after every default Plover theory English brief to translate the word to Australian English. For example, to write the American spelling of "empathize", you would stroke `*EPL/THAOEUS`. Then, to write "empathise" you would add `/A*U`. That is, this dictionary’s entry for "empathise" is `"*EPL/THAOEUS/A*U": "empathise",`. To use this dictionary, copy the [`dict-en-AU-with-extra-stroke.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/dict-en-AU-with-extra-stroke.json) file into your dictionary folder and add it to your Plover config after the default Plover dictionary.



### Notes on Design of and Changes in the Australian English Dictionary

- `A*ER` strokes the "aero" prefix for the Australian spelling of aeroplane
- `*EG` strokes the "eing" suffix for words such as "ageing"
- `*LG` strokes the "ling" suffix for words such as "labelling"
- `*LD` strokes the "led" suffix for words such as "labelled"
- `*EPLT` strokes the "ement" suffix for words such as "judgement", "acknowledgement", "lodgement" and "abridgement"
- `O*UR` strokes the "our" suffix for words such as "humour"
- `KWRO*R` strokes the "iour" suffix for words such as "behaviour"
- Add "U" to `O*R` or `TPHOR` strokes for "nour" endings in words such as "honour" e.g. `"HOPB/TPHOUR": "honour",`
- Add "U" to `O*R` or `TKOR` strokes for "dour" endings in words such as "candour" e.g. `"KAPBD/O*UR": "candour",`
- Add "U" to `O*R` or `KHROR` strokes for "our" endings in words such as "colour" e.g. `"KHROUR": "colour",`

- For words such as "practice" and "practise", the basic rule is that the noun form uses the "c" spelling while the verb uses the "s" spelling. Therefore, translations have been included for producing both.
    - For example, Australian briefs for "defense" with an "s" will use `S` in the brief itself, while Australian briefs for "defence" with a "c" will drop the `S`, eg, `"TKEFS": "defense"`, `"TKE/TPEPB": "defence"`.
    - As another example, drop the `S` or use `KRE` to spell licence with a "c", eg: `"HR-PB": "licence"`, `"HR-PBS": "license",`
- Use "AE" in strokes for Australian "ae" spellings such as "encyclopaedia":
    - The Australian spelling is used in words stroked with `AE` where it would normally use the long "e" sound stroke `AOE`
    - Briefs form the Australian spelling, eg, "KAOEUPL/RA": "chimaera",
    - Words starting with "ae" can be stroked with the prefix `A` such as `"A/AOE/O*PB": "aeon",`
    - The Australian spelling of "gynaecological" uses briefs and phonetic strokes beginning with `TKPWAOEUPB` => "gyne", while the US spelling uses strokes beginning with `SKWREUPB` => "jyn"



### Notes on Design of and Changes in the Australian English with Extra Strokes Dictionary

- `A*ER/A*U` strokes the "aero" prefix for the Australian spelling of aeroplane
- `*EG/A*U` strokes the "eing" suffix for words such as "ageing"
- `*LG/A*U` strokes the "ling" suffix for words such as "labelling"
- `*LD/A*U` strokes the "led" suffix for words such as "labelled"
- `*EPLT/A*U` strokes the "ement" suffix for words such as "judgement", "acknowledgement", "lodgement" and "abridgement"
- `O*UR/A*U` strokes the "our" suffix for words such as "humour"
- `KWRO*R/A*U` strokes the "iour" suffix for words such as "behaviour"
- Add "U" to `O*R/A*U` or `TPHOR/A*U` strokes for "nour" endings in words such as "honour" e.g. `"HOPB/TPHOUR/A*U": "honour",`
- Add "U" to `O*R/A*U` or `TKOR/A*U` strokes for "dour" endings in words such as "candour" e.g. `"KAPBD/O*UR/A*U": "candour",`
- Add "U" to `O*R/A*U` or `KHROR/A*U` strokes for "our" endings in words such as "colour" e.g. `"KHROUR/A*U": "colour",`



### Australian vocabulary

New briefs have also been added for Australian [diminuitives](https://en.wikipedia.org/wiki/Diminutives_in_Australian_English), flora, fauna, [slang and more](https://en.wikipedia.org/wiki/Australian_English_vocabulary). For example:

* `"STRA*EU": "Australia",`
* `"STRA*EU/KWRA": "straya",`
* `"PWOE/TKPWAPB": "bogan",`
* `"RE/PHOFL/EUFT": "removalist",`
* `"STRAO*UT": "strewth",`
* `"HROL/HREU": "lolly",`
* `"TKPWAE/TKAEU": "g'day",`
* `"RAO": "roo",`
* `"PHABG/KAS": "Maccas",`



### Changed Briefs

The brief for "programme" is overridden by "pram", requiring a new brief for "program":

    +"PRAPL": "pram",
    +"PRO/TKPWRAPL": "program",

The `*EG` brief for "e.g." is overridden by the "eing" suffix for the Australian spelling of "ageing", requiring a new brief for "e.g.":

    +"AOE/SKWRAO*E": "e.g.",



## Vim Dictionary

Copy the [`vim.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/vim.json) file into your dictionary folder and add it to your Plover config to use the following briefs. Note, most strokes use `STPR` to indicate vim (`SR` => `V`):

* `"SREUPL"`: Phonetic brief for "vim".
* `"SR*EUPL"`: Restore brief for "victim" using additional star.
* Punctuation with suppressed spaces to run vim commands (see also: unspaced punctuation dictionary):
    - `"P-P"`: Unspaced period for vim's "last edit" command.
    - `"T*EULD"`: Unspaced tilde for capitalisation. That is, `~`. This brief follows format for tilde `TEULD` with additional star.
    - `"TPHRORB"` => `FLOSH`: Unspaced dollar sign for end of line command.
    - `HR*PB`: Unspaced `<` for left indent.
    - `TKPWR*PB`: Unspaced `>` for right indent.
    - `KW-L`: Unspaced `=`.
    - `OEU`: Unspaced `/` for searching.
* `STPR` and `*`, `-B`, `-G`, `-R` for vim style navigation keys `hjkl`:
    - `"STPR*"`: `h`
    - `"STPR-B"`: `k`
    - `"STPR-G"`: `l`
    - `"STPR-R"`: `j`
    - `"STPR*B"`: `⌃f` to page forward
    - `"STPR*P"`: `⌃b` to page backward
* Move lines up and down in any mode:
    - `.vimrc` mappings are:

            " Move lines up/down using alt j/k when iTerm is set to:
            " Left option (⌥) key acts as Normal
            " In mapping, press opt/alt+j/k to type these characters
            nnoremap ∆ :m .+1<CR>
            nnoremap ˚ :m .-2<CR>

            inoremap ∆ <Esc>:m .+1<CR>gi
            inoremap ˚ <Esc>:m .-2<CR>gi

            vnoremap ∆ :m '>+1<CR>gv=gv
            vnoremap ˚ :m '<-2<CR>gv=gv

    - Briefs are:
        - `"PHR-B"` => `MLB`: Move line up using vim style navigation `k`.
        - `"PHR-R"` => `MLR`: Move line down using vim style navigation `j`.
* `"SPWAO*UT"`: Exit insert mode and start substitution. That is, Escape and `:%s/`.
* `"SR*F"`: Exit insert mode and run command to write buffer (i.e. save the file). That is, Escape, `:w`, and Return. Brief format follows brief for Save command `"S*F"`.
* `"STPR*F"`: Exit insert mode and run command to write buffer (i.e. save the file). That is, Escape, `:w`, and Return. This alternative brief format follows brief for Save command `"S*F"` combined with brief format for most of these vim strokes using `STPR`.
* `"STPROEUFRL"`: Steno lookup shortcut that exits insert mode, yanks inside word to system clipboard (this might be Neovim only) using `"yiw` and runs my shortcut for steno lookup tool `⌃⌘⌥⇧s`. Brief format combines vim brief and regular steno lookup brief `STOEUFRL`. To use your own shortcut, replace this part of the translation `{#Control_L(Alt_L(Shift_L(Super_L(s))))}` with your shortcut command.
* `"STPREFBG"`: Exit insert mode and prepare command to write buffer (i.e. save the file) and quit. That is, Escape and `:x`. Brief format follows vim brief format `STPR` and brief for Escape `TPEFBK`.
* `"STPR-FPLT"`: Exit insert mode and write unspaced colon to enter command mode. That is, Escape and `:`.
* `"STPR-L"`: Runs `gt` to go to next tab. Follows brief format of tabs from tab navigation dictionary.
* `"STPR-F"`: Runs `gT` to go to previous tab. Follows brief format of tabs from tab navigation dictionary.

* Quickfix list “command do” to execute `{cmd}` in each entry of the list: `"KHRO*D": "cdo",`
* Vertical split screen: `"SR*EUP": ":vsp{#Return}",`
* Ignore case in search: `"OEU/KRO*EU": "{^/\\c^}",`
* `"SREUPL/KWRUPL": "vimium",`
* `"SRUPBLD": "vundle",`
* `"PWUPBLD": "bundle",`
* `"PHRUG": "plug",`

* Single-stroke Control key (`⌃`) fingerspelling modifier collection:
    - `"A*RBL": "{#Control_L(a)}",`
    - `"PW*RBL": "{#Control_L(b)}",`
    - `"KR*RBL": "{#Control_L(c)}",`
    - `"TK*RBL": "{#Control_L(d)}",`
    - `"*ERBL": "{#Control_L(e)}",`
    - `"TP*RBL": "{#Control_L(f)}",`
    - `"TKPW*RBL": "{#Control_L(g)}",`
    - `"H*RBL": "{#Control_L(h)}",`
    - `"*EURBL": "{#Control_L(i)}",`
    - `"SKWR*RBL": "{#Control_L(j)}",`
    - `"K*RBL": "{#Control_L(k)}",`
    - `"HR*RBL": "{#Control_L(l)}",`
    - `"PH*RBL": "{#Control_L(m)}",`
    - `"TPH*RBL": "{#Control_L(n)}",`
    - `"O*RBL": "{#Control_L(o)}",`
    - `"P*RBL": "{#Control_L(p)}",`
    - `"KW*RBL": "{#Control_L(q)}",`
    - `"R*RBL": "{#Control_L(r)}",`
    - `"S*RBL": "{#Control_L(s)}",`
    - `"T*RBL": "{#Control_L(t)}",`
    - `"*URBL": "{#Control_L(u)}",`
    - `"SR*RBL": "{#Control_L(v)}",`
    - `"W*RBL": "{#Control_L(w)}",`
    - `"KP*RBL": "{#Control_L(x)}",`
    - `"KWR*RBL": "{#Control_L(y)}",`
    - `"STKPW*RBL": "{#Control_L(z)}",`

* `"RO*RB"` to hit Return, Escape, and O for leaving cursor inside a function after writing a pair of brackets.
* `"TPH*EG"` to move to the next markdown header and move that heading’s line to the top of the window using [vim-markdown](https://github.com/dimonster/vim-markdown)
* `"SROEUPBD": "{^}ys{^}",` and `"SRO*EUPBD": "{^}yS{^}",` for yank surround using [vim-surround](https://github.com/tpope/vim-surround)
`"KHRO*D/SPWAO*UT"` to use `cdo` and `s###g | w` substitute with a write between each substitution.
* `"STPREG"` and `STPR*EG` to go to next and previous errors (using `:cn` and `:cp`).



## Git Dictionary

Copy the [`git.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/git.json) file into your dictionary folder and add it to your Plover config to use the following briefs:

* "git" `TKPWEUT`
* "add" `AD`
* " " `S-P`
* "dict" `TKEUBGT`
* " ." `P-P`
* "JSON" `SKWRO*FPB`
* "status" `ST*TS`
* "diff" `TKEUF`
* " --" `TK*RB`
* "cached" `KAERBD`
* "commit" `KPHEUT`
* " -" `H*PB`
* "v" `SR*`
* "log" `HROG`
* "p" `P*`
* "push" `PURB`
* "origin" `O*RPBLG`
* "master" `PHAFRT`
* "pull" `PUL`
* "{re^}" `RE`
* "base" `PWAEUS`
* "check" `KHEBG`
* "-out" `O*UT`
* "hot" `HOT`
* delete space `TK-LS`
* "fix `TPEUBGS`
* "reset" `RE/SET`
* "HEAD" `KPA*E/HED`
* "^" `KR-RT`
* "/" `OEU`
* "gitignore" `TKPWEUT/EUG`
* "mergetool" `PHERPBLGT`
* "checkout" `KHEBGT`



## Ruby Dictionary

Copy the [`ruby.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/ruby.json) file into your dictionary folder and add it to your Plover config to use the following briefs:

* "%>" `*ERB/KHRO*EZ` (<strong>ERB close</strong>ing tag)
* "<%=" `*ERB/KPEBG` (<strong>ERB</strong> e<strong>xec</strong>ute tag)
* "<%" `*ERB/O*EP` (<strong>ERB open</strong>ing tag)
* "utf-" `*UFT`
* "utf-8" `*UFT/#L`
* "UTF-" `*UFT/*UFT`
* "ARGV" `A*RG/SR*`
* "ARGF" `A*RG/TP*`
* "attr_accessor" `A*RT/KPES` (<strong>attr</strong> _ ac<strong>cess</strong>or)
* "attr_reader" `A*RT/RAERD` (<strong>attr</strong> _ <strong>reader</strong>)
* "attr_writer" `A*RT/WREUR` (<strong>attr</strong> _ <strong>writer</strong>)
* "after_filter" `AF/TP*EURLT` (<strong>af</strong>ter <strong>filter</strong>)
* "before_filter" `PW-FR/TP*EURLT` (<strong>befor</strong>e <strong>filter</strong>)
* "ERB" `ERB`
* "=>" `HARB/RO*BGT` (<strong>hash rocket</strong>)
* "https://rubygems.org" `HAOEPTS/RO*EUB/SKWREPLS`
* "<<-" `HAOER/TKO*BG` (<strong>heredoc</strong>)
* "<<-ERROR" `HAOER/TKO*BG/ROEUR` (<strong>heredoc</strong> e<strong>rror</strong>)
* "::" `KHR-PBS`  (<strong>c</strong>o<strong>lons</strong>)
* ".html.erb" `P-P/HAOEPLT/ERB`
* "params[:" `PRA*PLS/PWR-BGT`
* "rspec" `R*/SP*EBG`
* "rspec-rerun:spec" `R*/SP*EBG/RE/RUPB/SP*EBG`
* "rspec-rerun/tasks" `R*/SP*EBG/RE/RUPB/TAFBGS`
* "regex" `REG/EBG`
* "regexp" `REG/EBGS`
* "rubygems" `RO*EUB/SKWREPLS`
* "def" `TK-F`
* "nokogiri" `TPHO/KO/TKPWEU/REU`
* "flash[:" `TPHRARB/PWR-BGT`
* "flash[:error]" `TPHRARB/PWR-BGT/ROEUR`
* "flash[:success]" `TPHRARB/PWR-BGT/SKES`
* "flash[:notice]" `TPHRARB/PWR-BGT/TPH-TS`



## Technical Dictionaries

- Copy the [`html.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/html.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"HR*EF": "href",`.
- Copy the [`css-alignment.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/css-alignment.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"TPHREBGS": "flex",`.
- Copy the [`css-declarations.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/css-declarations.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"KA*LG": "calc",`.
- Copy the [`css-media-object.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/css-media-object.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"*EUPBLG": "img",`.
- Copy the [`javascript.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/javascript.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"TKPWET/EL/*EPLT/PWEU/EUD": "getElementById",`.
- Copy the [`react.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/react.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"TH-P/SET/STA*ET/PR*EPBS": "{>}this.setState()",`.
- Copy the [`python.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/python.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"PAOEU/S*FR": "python -m SimpleHTTPServer",`.
- Copy the [`ux-design.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/ux-design.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"AOUBLT": "usability",`.
- Copy the [`sketch-app.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/sketch-app.json) file into your dictionary folder and add it to your Plover config to use the briefs like: `"SK*EFP/PHR-P": "{#Alt_L(Super_L(Up))}",` to move layers.
- Copy the [`code.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/code.json) file into your dictionary folder and add it to your Plover config to use various briefs relating to coding and the command line.



## Common Words Dictionary

This dictionary consists of common words already available in the default Plover dictionary. If you need only the common words for some reason, copy the [`common-words.json`](https://github.com/dimonster/plover-dictionaries/raw/master/dictionaries/common-words.json) file into your dictionary folder and add it to your Plover config to use the briefs for a thousand or so common English words.



# Contributing

If you notice a misstroke, please mention it. This will help future stenographers learning from Typey Type for Stenographers have a better experience learning stenography. The easiest way to help is to [create a new issue](https://github.com/dimonster/steno-dictionaries/issues/new) for each misstroke or set of misstrokes you find.



## Better briefs

When proposing better briefs, here are some suggestions:

- Check your dictionary for similar strokes. There might be unexpected conflicts around your preferred brief.
- Check your dictionary for similar word beginnings and endings. There might be a set of relevant strokes that suggest a better brief. There might also be similar words that need new briefs at the same time to be consistent.
- Check for potential conflicts or word boundary errors, especially when using strokes used for prefixes or suffixes.
- Ask the [community](http://www.openstenoproject.org/community/) for suggestions.



## Looking for misstrokes

- Words containing "b" with a stroke that is missing P or W is probably a misstroke. You can search for that with a regex like one of these:

```
/.*P[^W]\+[AOEU*-]\+.*": ".*b.*"
/.*[^P]W\+[AOEU*-]\+.*": ".*b.*"
```

- Strokes containing `OEU` that aren't used for "oi" sounds like "boy" or "oil" are probably a misstroke:

```
/[^A]OEU.*": "[^o][^iy]\+",
```



# Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [typeytype@didoesdigital.com](mailto:typeytype@didoesdigital.com).



# License

GPLv2+. See [license](LICENSE) for details.

