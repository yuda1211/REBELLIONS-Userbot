from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node

@register(outgoing=True, pattern='^RB(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**REBELLIONS LEWAT NIH MONYET!!!**")

\n\n`RB`\
\nUsage: Hujat Jamet.\
})
