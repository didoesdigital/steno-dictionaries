---
name: Misstrokes
about: Create an issue to track and improve misstrokes or other problems with entries
  in these dictionaries
title: "`example misstroke entry` misstrokes"
labels: ''
assignees: ''

---

Hello! Thanks for contributing! Your contribution will help new stenographers learn stenography and have a much better experience while they learn. Before you submit this issue, please check existing open and closed issues to make sure there are no duplicates. Feel free to use this template or start from scratch.



# Dictionary

I noticed this dictionary entry or these dictionary entries in:

- `dict.json`
- `dict-en-AU-with-extra-stroke.json`



# Misstroked entry or entries

This looks like a misstroke or could otherwise be better:

```json
"TEFT/KP-PL/PHEUS/STROBG/EP/TREU": "example misstroke entry",
"TEFT/KP-PL/PHEUS/STROBG/EP/TREU/A*U": "example misstroke entry",
```

This looks like a misstroke because:

- "test" does not appear in the translation, as suggested by `TEFT`.
- "entry" is missing a `B` in `EP` for a phonetic stroke.
- "entry" could use the brief `SPWREU`.
- "mis" is not using the prefix stroke `PHEUZ`.
- "stroke" is missing an `E` in `STROEBG`, which would be the phonetic, Plover theory stroke.
- It could cause a conflict trying to write "test example misstroke entry".



# Expected

I would expect the outline to be:

```json
"KP-PL/PHEUZ/STROEBG/SPWREU": "example misstroke entry",
```

I would expect to see that outline because:

- It uses a prefix stroke.
- It is consistent with the `main.json` dictionary from Plover 3.
- The phonetic stroke for "stroke" is written using `STROEBG`, which is consistent with the strokes used for "brushstroke", "heatstroke", and "sunstroke".
- Mirabai says…



# Even better

To make this even better, we could:

- Remove the entry completely because it can already be stroked without its own entry. It is not a common phrase so it does not need to appear in dictionary look up searches.
- Remove the stroke `STROBG` for "stroke" to be consistent with others, even though it is common in Plover theory to use the single vowel letter stroke when there's no other adjacent vowel in the translation.
