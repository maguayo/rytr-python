from rytr.helpers import post


class Content:
    @staticmethod
    def generate(
        language_id,
        tone_id,
        usecase_id,
        input_contexts,
        user_id,
        variations=1,
        format="text",
        creativityLevel="default",
    ):
        return post(url="ryte", data={
            "languageId": language_id,
            "toneId": tone_id,
            "useCaseId": usecase_id,
            "inputContexts": input_contexts,
            "userId": user_id,
            "variations": variations,
            "format": format,
            "creativityLevel": creativityLevel,
        })
