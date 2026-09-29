import streamlit as st
import requests

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"

st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .title {
        text-align: center;
        color: #1f2937;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 30px;
    }

    div.stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">💻 Laptop Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter laptop specifications to estimate its price</div>',
    unsafe_allow_html=True
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🏢 Basic Information")

    company = st.selectbox(
        "Company",
        [
        "Dell",
        "Lenovo",
        "HP",
        "Asus",
        "Acer",
        "MSI",
        "Toshiba",
        "Apple",
        "Samsung",
        "Razer",
        "Mediacom",
        "Microsoft",
        "Xiaomi",
        "Vero",
        "Chuwi",
        "Google",
        "Fujitsu",
        "LG",
        "Huawei"
        ]
    )

    typename = st.selectbox(
        "TypeName",
        [
            "Notebook",
            "Ultrabook",
            "Gaming",
            "2 in 1 Convertible",
            "Workstation",
            "Netbook"
        ]
    )

    ram = st.selectbox(
        "RAM (GB)",
        [2, 4, 6, 8, 12, 16, 24, 32, 64],
        index=3
    )

    touchscreen = st.selectbox(
        "TouchScreen",
        ["NO", "YES"]
    )

    ips = st.selectbox(
        "IPS",
        ["NO", "YES"]
    )

with col2:
    st.subheader("🖥️ Display & Storage")

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.5,
        max_value=6.0,
        value=2.0,
        step=0.1
    )

    screenresolution = st.selectbox(
        "Screen Resolution",
        [
            "1366x768",
            "1600x900",
            "1920x1080",
            "2304x1440",
            "2400x1600",
            "2560x1440",
            "2376x1824",
            "3200x1800",
            "3840x2160",
            "2560x1600",
            "2880x1800",
            "3072x1920",
            "2256x1504"
        ]
    )

    screensize = st.number_input(
        "Screen Size (inch)",
        min_value=10.0,
        max_value=20.0,
        value=15.6,
        step=0.1
    )

    hard_drive = st.selectbox(
        "Hard Drive (GB)",
        [0, 128, 256, 500, 512, 1000, 2000]
    )

    ssd = st.selectbox(
        "SSD (GB)",
        [0, 128, 256, 512, 1000, 2000]
    )

with col3:
    st.subheader("⚙️ Hardware")

    opsys = st.selectbox(
        "Operating System",
        [
            "Windows",
            "Mac",
            "Others/No OS/Linux"
            
        ]
    )

    cpu_name = st.selectbox(
        "CPU",
        [
            "Intel Core i3",
            "Intel Core i5",
            "Intel Core i7",
            "Intel Core i9",
            "AMD",
            "Other Intel Processor"
        ]
    )

    gpu_name = st.selectbox(
        "GPU",
        [
            "Intel",
            "Nvidia",
            "AMD",
            
        ]
    )

st.divider()

st.subheader("🔮 Get Price Prediction")

if st.button("Predict Laptop Price"):

    payload = {
        "company": company,
        "TypeName": typename,
        "Ram": int(ram),
        "TouchScreen": touchscreen,
        "IPS": ips,
        "weight": weight,
        "Screenresolution": screenresolution,
        "Screensize": screensize,
        "Hard_drive": int(hard_drive),
        "ssd": int(ssd),
        "opsys": opsys,
        "cpu_name": cpu_name,
        "gpu_name": gpu_name
    }

    try:
        with st.spinner("Predicting price..."):
            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

        if response.status_code == 200:
            result = response.json()

            prediction = result.get(
                "prediction",
                result.get("Price")
            )

            st.success("Prediction successful! 🎉")

            st.metric(
                label="Estimated Laptop Price",
                value=f"₹ {float(prediction):,.2f}"
            )

        else:
            st.error(f"API Error: {response.status_code}")
            st.code(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server.")
        st.info("Make sure your FastAPI server is running.")

    except requests.exceptions.Timeout:
        st.error("The request timed out. Please try again.")

    except Exception as e:
        st.error("Something went wrong.")
        st.code(str(e))

st.divider()

st.caption("Laptop Price Prediction • Streamlit + FastAPI")
