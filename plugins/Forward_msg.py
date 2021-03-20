import nonebot
from nonebot import on_natural_language, permission, NLPSession


@on_natural_language(only_to_me=False, permission=permission.GROUP)
async def _(session: NLPSession):
    bot = nonebot.get_bot()
    print(str(session.ctx['group_id']), str(session.ctx['user_id']))
    print(str(session.ctx))
    if session.ctx['group_id'] == 457017628 and session.ctx['user_id'] in [2454398382, 3014234468]:
        # 发送到群
        await bot.send_group_msg(group_id=653685985, message=str(session.msg))
        # 发送到人
        # await bot.send_msg(user_id=3407402583, message=str(session.msg))
        return
