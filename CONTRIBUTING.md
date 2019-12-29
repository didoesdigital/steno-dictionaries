# Contributing to Steno Dictionaries

🎉 Thanks for taking the time to contribute! 🎉

## Issues

You can [create a new issue](https://github.com/didoesdigital/steno-dictionaries/issues/new) to track misstrokes or other problems with entries in these dictionaries.

## Development

### Open issues before Pull Requests

If it’s your first contribution to this project, please create an open issue and wait for a response before creating a Pull Request.

### Pull Requests

When removing misstrokes, check the following:

- The same misstrokes may appear in top words dictionaries and Australian English dictionaries and should be removed from them as well.
- There may be similar outlines that are also misstrokes and should be removed as well.
- If it’s a misstroke that someone might want to keep to effectively auto-correct typos, move it to the `bad-habits.json` dictionary.
- If it’s a truly bad entry (for example, the stroke does not follow steno order), delete it without adding it to the `bad-habits.json` dictionary.

Don’t edit the `misstrokes.json` dictionary by hand. The [`misstrokes.json`](https://github.com/didoesdigital/steno-dictionaries/raw/master/dictionaries/misstrokes.json) dictionary is an automated dictionary created from entries deleted out of [`dict.json`](https://github.com/didoesdigital/steno-dictionaries/raw/master/dictionaries/dict.json) that haven't been moved to other dictionaries.

If there’s no valid entry for a word in the latest Plover dictionary, consider the following:

- You might add a fingerspelling entry to the `condensed-strokes.json` dictionary. For example, see `"S*/P*/A*/K*/*E": "spake",` in closed issue [#47](https://github.com/didoesdigital/steno-dictionaries/issues/47).
- You might assemble an entry using existing words and prefix or suffix strokes. For example, `PHAFRPB` already translates to `march` and `*ER` already translates to the suffix `{^er}`, so you can assemble them into a new entry `"PHAFRPB/*ER": "marcher",` in the `condensed-strokes.json` dictionary to improve lookups.
- If it can be written using Plover’s orthography rules without an explicit entry, you might add an entry to improve lookups. For example, see `"SELTD": "settled",` in [#29](https://github.com/didoesdigital/steno-dictionaries/pull/29). This example “tucks” or “folds” the `-D` into the main outline `SELT` for `settle`. There is a risk that the seemingly free outline of `SELTD` in Plover’s main dictionary will one day be filled with a brief for something else. Use this approach with caution.

## Sponsor

You can support [Di’s efforts on Patreon](https://www.patreon.com/didoesdigital). A monthly donation helps Di build more lessons and features to help you fast-track your steno progress.

## Support

For questions about contributing, create an [issue](https://github.com/didoesdigital/steno-dictionaries/issues) or <a href="mailto:typeytype@didoesdigital.com">email typeytype@didoesdigital.com</a>.

