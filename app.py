import streamlit as st
from google import genai

st.set_page_config(page_title="مصحح النصوص العربي", layout="centered")

st.title("✍️ مصحح النصوص الذكي")
st.write("أدخل النص العربي أدناه للحصول على التصحيح اللغوي والإملائي.")

# الحصول على المفتاح من Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("لم يتم العثور على مفتاح API! يرجى إضافته في Settings -> Secrets")
else:
    client = genai.Client(api_key=api_key)

    user_text = st.text_area("النص المراد تصحيحه:", height=150)

    if st.button("تصحيح النص"):
        if user_text.strip():
            with st.spinner("جاري تصحيح النص..."):
                try:
                    prompt = f"قم بتصحيح الأخطاء الإملائية والنحوية في النص التالي مع الحفاظ على المعنى:\n{user_text}"
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=prompt,
                    )
                    st.success("تم التصحيح بنجاح!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال بالخدمة: {e}")
        else:
            st.warning("يرجى كتابة نص أولاً.")
