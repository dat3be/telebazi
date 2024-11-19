from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler  # Import ConversationHandler here
from modules.bazi_calculator import calculate_stem_and_branch, calculate_stem_and_branch_for_month, calculate_stem_and_branch_for_day, calculate_stem_and_branch_for_hour
from modules.date_utils import convert_solar_to_lunar
from modules.constants import DATE, TIME  # Import constants here
import logging

logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f"Started conversation with user_id: {user.id}, {user.first_name} {user.last_name}")
    await update.message.reply_text(
        "Chào bạn! Vui lòng nhập ngày tháng năm sinh của bạn (theo định dạng dd/mm/yyyy):"
    )
    return DATE

async def get_date(update: Update, context: CallbackContext) -> int:
    user_input = update.message.text
    user = update.message.from_user
    logger.debug(f"User {user.id} provided date input: {user_input}")

    try:
        day, month, year = map(int, user_input.split('/'))
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            context.user_data['date'] = (day, month, year)
            logger.info(f"User {user.id} successfully entered date: {day}/{month}/{year}")
            await update.message.reply_text(
                "Cảm ơn bạn! Vui lòng nhập giờ sinh của bạn (theo định dạng HH:MM):"
            )
            return TIME
        else:
            logger.warning(f"User {user.id} entered invalid date: {user_input}")
            await update.message.reply_text(
                "Ngày tháng năm không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy:"
            )
            return DATE
    except ValueError as e:
        logger.error(f"User {user.id} entered invalid date format: {user_input}. Error: {str(e)}")
        await update.message.reply_text(
            "Định dạng không đúng. Vui lòng nhập lại theo định dạng dd/mm/yyyy:"
        )
        return DATE

async def get_time(update: Update, context: CallbackContext) -> int:
    user_input = update.message.text
    user = update.message.from_user
    logger.debug(f"User {user.id} provided time input: {user_input}")

    try:
        hour, minute = map(int, user_input.split(':'))

        if 0 <= hour < 24 and 0 <= minute < 60:
            context.user_data['time'] = (hour, minute)
            date = context.user_data['date']
            lunar_date = convert_solar_to_lunar(date[2], date[1], date[0])

            # Calculate Heavenly Stem and Earthly Branch for the lunar year, month, day, and hour
            year_stem, year_branch = calculate_stem_and_branch(lunar_date.year)
            month_stem, month_branch = calculate_stem_and_branch_for_month(lunar_date.year, date[1])
            day_stem, day_branch = calculate_stem_and_branch_for_day(lunar_date.year, date[2])
            hour_stem, hour_branch = calculate_stem_and_branch_for_hour(lunar_date.year, hour)

            logger.info(f"User {user.id} successfully entered time: {hour}:{minute}")
            await update.message.reply_text(
                f"Ngày sinh của bạn là {lunar_date.day}/{lunar_date.month}/{lunar_date.year} âm lịch.\n"
                f"Năm: {year_stem} {year_branch}.\n"
                f"Tháng: {month_stem} {month_branch}.\n"
                f"Ngày: {day_stem} {day_branch}.\n"
                f"Giờ: {hour_stem} {hour_branch}."
            )
            return ConversationHandler.END
        else:
            logger.warning(f"User {user.id} entered invalid time: {user_input}")
            await update.message.reply_text(
                "Giờ sinh không hợp lệ. Vui lòng nhập lại theo định dạng HH:MM (Giờ từ 00-23, Phút từ 00-59):"
            )
            return TIME

    except ValueError as e:
        logger.error(f"User {user.id} entered invalid time format: {user_input}. Error: {str(e)}")
        await update.message.reply_text(
            "Định dạng không đúng. Vui lòng nhập lại theo định dạng HH:MM (Giờ từ 00-23, Phút từ 00-59):"
        )
        return TIME


async def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f"User {user.id} cancelled the conversation.")
    await update.message.reply_text('Cuộc trò chuyện đã kết thúc.')
    return ConversationHandler.END
