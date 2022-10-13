import random

from razan.strings.fun import *
from sbb_b import sbb_b
from sbb_b.core.managers import edit_or_reply
from sbb_b.helpers import get_user_from_event

from . import *


@sbb_b.ar_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بقلبك 🖤 "
    )


@sbb_b.ar_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم الزواج اعملو واحد بقا 🤤😂",
    )


@sbb_b.ar_cmd(pattern="رفع متوحد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**- احا دا المبرمج صلاح حمدان يفشخني انا وانت لو عملتها 😂💔 **")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**- احا دا المبرمج صلاح حمدان يفشخني انا وانت لو عملتها 😂💔**")
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**- احا دا المبرمج بيكاتشو يسطا 😂💔**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه متوحد كنت شاكك فيه اصلا 😂 "
    )


@sbb_b.ar_cmd(pattern="رفع وتكه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**- احا دا المبرمج صلاح انت عبيط**")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**- احا دا المبرمج صلاح انت عبيط**")
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**- احا دا المبرمج بيكاتشو انت عبيط **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـها وتكه في الجروب 😹🤤",
    )


@sbb_b.ar_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه جلب خليه خله ينبح 😂🐶",
    )


@sbb_b.ar_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@sbb_b.ar_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@sbb_b.ar_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@sbb_b.ar_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه تاج 👑🔥"
    )


@sbb_b.ar_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**- احا دا مبرمج السورس انت عبيط يسطا**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@sbb_b.ar_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@sbb_b.ar_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@sbb_b.ar_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5372193406:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**100%**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه حيوان 🐏"
    )


@sbb_b.ar_cmd(pattern="رفع قطه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه قطه 🐈"
    )


@sbb_b.ar_cmd(pattern="رفع زاحف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🐍💞"
    )


@sbb_b.on(admin_cmd(pattern="نتجوز(?:\s|$)([\s\S]*)"))
async def rzfun(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5646258337:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس قلبه لبسكوته بس 🥹♥**")
    await edit_or_reply(mention, f"**زواج مبروك بس متبصش على غيري 🥺💞 ܰ**")


@sbb_b.on(admin_cmd(pattern="طلاق(?:\s|$)([\s\S]*)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5768182096:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await edit_or_reply(mention, f"**طالق طالق بالعشرة 😹😭💕 ܰ**")
