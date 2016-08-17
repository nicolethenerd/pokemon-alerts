# Pokelerts

Alerts for Pokemon Go!

To use:

1. Open the file and modify the `pokemonList` to set pokemon you care about to `True`, and those you don't to `False`
2. Set the `bounds` variable to bound a small rectangle around your own latitude and longitude.
3. Use cron or launchd to run this program at a set interval, by having it call `python pokelert.py`. I have mine run every 5 minutes.
