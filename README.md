# learned-words-discord-bot
A bot to manage learned words in English, their translation and meaning. Offers a regular rotation of words to be posted to a designated channel as a language learning refresher.

## 0.X Command List
### Generic Commands
 - `!help`
 - `!learn "<word>" "<translation>" "<optional definition>"`
 - `!unlearn <word>`
 - `!translate <word or translation>`
### Recap Commands
 - `!enable_recap`
 - `!disable_recap`
 - `!recap`

## 1.x Roadmap
**These commands are just a roadmap, they do not currently exist.**

The initial release of the bot will handle a simple A to B translation 
with no accounting for languages, the second version of the bot will allow
users to store words against ISO-639-1 codes to allow flexibility of multiple 
translations and lookups.

### Language Commands
- `!languages`
- `!language search_term`
### Language Specific Commands
 - `!add_word en:word ja:word tl:word`
 - `!remove_word code:word`
### Recap Commands
 - `!recap_hours [number of hours]`
 - `!recap <language>`
 ### Settings Commands
 - `!default_language en`