from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

async def summarize_with_gpt4(content: str) -> str:
    try:
        # GPT-4로 텍스트 요약하기
        response = openai.Completion.create(
            engine="text-davinci-003", # GPT-4에 해당하는 최신 엔진을 사용하세요.
            prompt=f"요약: {content}\n\nTL;DR:",
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        print(f"Error while summarizing with GPT-4: {e}")
        return "요약 중 오류 발생"

# 가상의 블로그 게시 함수
async def mock_post_to_blog(summary: str) -> dict:
    # 실제로는 여기에서 블로그 플랫폼의 API를 호출하여 요약된 내용을 게시합니다.
    # 이 예제에서는 게시가 '성공적으로 완료되었다'는 가정 하에 실행됩니다.
    return {"status": "success", "message": "Post successfully published!"}

@app.post("/summarize-newsletter")
async def summarize_newsletter(content: str):
    try:
        summary = await summarize_with_gpt4(content)
        post_result = await mock_post_to_blog(summary)
        return {"summary": summary, "post_result": post_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def read_root():
    return {"Hello": "World"}
