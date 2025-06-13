import streamlit as st

# ----------------------------
# DATA
# ----------------------------
DATA = {
    # Name:   (time_s, {tier: payout_per_cycle, ...})
    'Noob':             {'Normal':0.25,  'Gold':0.38,  'Rainbow':0.50,  'Inferno':0.75,  'Oblivion':1.00,   'Celestial':1.25},
    'Businessman':      {'Normal':1.25,  'Gold':1.88,  'Rainbow':2.50,  'Inferno':3.75,  'Oblivion':5.00,   'Celestial':6.25},
    'Teacher':          {'Normal':2.00,  'Gold':3.00,  'Rainbow':4.00,  'Inferno':6.00,  'Oblivion':8.00,   'Celestial':10.00},
    'Builder':          {'Normal':2.00,  'Gold':3.00,  'Rainbow':4.00,  'Inferno':6.00,  'Oblivion':8.00,   'Celestial':10.00},
    'Gardener':         {'Normal':2.50,  'Gold':3.75,  'Rainbow':5.00,  'Inferno':7.50,  'Oblivion':10.00,  'Celestial':12.50},
    'Painter':          {'Normal':7.50,  'Gold':11.25, 'Rainbow':15.00, 'Inferno':22.50, 'Oblivion':30.00,  'Celestial':37.50},
    'Chef':             {'Normal':10.50, 'Gold':15.75, 'Rainbow':21.00, 'Inferno':31.50, 'Oblivion':42.00,  'Celestial':52.50},
    'Mine':             {'Normal':15.75, 'Gold':23.63, 'Rainbow':31.50, 'Inferno':47.25, 'Oblivion':63.00,  'Celestial':78.75},
    'Fortunemagician':  {'Normal':30.00, 'Gold':45.00, 'Rainbow':60.00, 'Inferno':90.00, 'Oblivion':120.00, 'Celestial':150.00},
    'Bank':             {'Normal':75.00, 'Gold':112.50,'Rainbow':150.00,'Inferno':225.00,'Oblivion':300.00, 'Celestial':375.00},
    'Skyscraper':       {'Normal':150.00,'Gold':225.00,'Rainbow':300.00,'Inferno':450.00,'Oblivion':600.00, 'Celestial':750.00},
    'Stadium':          {'Normal':457.14,'Gold':685.71,'Rainbow':914.29,'Inferno':1371.43,'Oblivion':1828.57,'Celestial':2285.71},
    'Waterpark':        {'Normal':1333.33,'Gold':2000.00,'Rainbow':2666.67,'Inferno':4000.00,'Oblivion':5333.33,'Celestial':6666.67},
    'Castle':           {'Normal':6550.00,'Gold':9825.00,'Rainbow':13100.00,'Inferno':19650.00,'Oblivion':26200.00,'Celestial':32750.00},
    'Club':             {'Normal':10000.00,'Gold':15000.00,'Rainbow':20000.00,'Inferno':30000.00,'Oblivion':40000.00,'Celestial':50000.00},
    'Airport':          {'Normal':48000.00,'Gold':72000.00,'Rainbow':96000.00,'Inferno':144000.00,'Oblivion':192000.00,'Celestial':240000.00},
    'Eggtrader':        {'Normal':85.00, 'Gold':127.50,'Rainbow':170.00,'Inferno':255.00,'Oblivion':340.00,  'Celestial':425.00},
    'Crystalcarver':     {'Normal':3833.33,'Gold':5750.00,'Rainbow':7666.67,'Inferno':11500.00,'Oblivion':15333.33,'Celestial':19166.67},
    'Dragon':           {'Normal':48333.33,'Gold':72500.00,'Rainbow':96666.67,'Inferno':145000.00,'Oblivion':193333.33,'Celestial':241666.67},
    'Astronaut':        {'Normal':125.00,'Gold':187.50,'Rainbow':250.00,'Inferno':375.00,'Oblivion':500.00,  'Celestial':625.00},
    'Aliengardener':    {'Normal':180.00,'Gold':270.00,'Rainbow':360.00,'Inferno':540.00,'Oblivion':720.00,  'Celestial':900.00},
    'Ufo':              {'Normal':500.00,'Gold':750.00,'Rainbow':1000.00,'Inferno':1500.00,'Oblivion':2000.00,'Celestial':2500.00},
    'Blackhole':        {'Normal':4000.00,'Gold':6000.00,'Rainbow':8000.00,'Inferno':12000.00,'Oblivion':16000.00,'Celestial':20000.00},
    'Galaxy':           {'Normal':10000.00,'Gold':15000.00,'Rainbow':20000.00,'Inferno':30000.00,'Oblivion':40000.00,'Celestial':50000.00}
    }

MANAGER_BOOSTS = {
    'Clown': 1.2,
    'Soldier': 1.4,
    'Mayor': 1.6,
    'King': 2.0,
    'Modern': 2.4,
    'Fairy': 2.6,
    'Angel': 3.0
}

# ----------------------------
# INIT SESSION STATE
# ----------------------------
if 'buildings' not in st.session_state:
    st.session_state.buildings = []

# ----------------------------
# SIDEBAR BOOST OPTIONS
# ----------------------------
st.sidebar.title("📈 Boost Options")
manager = st.sidebar.selectbox("Manager Boost", list(MANAGER_BOOSTS.keys()), index=5)
friends = st.sidebar.number_input("Number of Friends (0–5)", min_value=0, max_value=5, value=0)
premium = st.sidebar.checkbox("Premium Boost (+10%)")

# ----------------------------
# MAIN INTERFACE
# ----------------------------
st.title("🏗️ Grow a Business Earnings Calculator")
st.markdown("Add buildings, select boosts, and calculate your income.")

col1, col2, col3 = st.columns(3)
with col1:
    building = st.selectbox("Building", list(DATA.keys()))
with col2:
    tier = st.selectbox("Tier", ["Normal", "Gold", "Rainbow", "Inferno", "Oblivion", "Celestial"])
with col3:
    count = st.number_input("Count", min_value=1, value=1)

if st.button("➕ Add Building"):
    st.session_state.buildings.append((count, tier, building))

# ----------------------------
# DISPLAY BUILDING LIST
# ----------------------------
if st.session_state.buildings:
    st.subheader("📦 Your Buildings")
    for i, (cnt, tier, name) in enumerate(st.session_state.buildings):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"{cnt}× {tier} {name}")
        with col2:
            if st.button("❌ Remove", key=f"remove_{i}"):
                st.session_state.buildings.pop(i)
                st.rerun()
    if st.button("🗑️ Clear All Buildings"):
        st.session_state.buildings.clear()
        st.rerun()
else:
    st.info("No buildings added yet.")

# ----------------------------
# CALCULATE TOTALS
# ----------------------------
if st.button("🧮 Calculate Earnings"):
    manager_boost = MANAGER_BOOSTS[manager]
    friend_boost = 1 + 0.05 * friends
    premium_boost = 1.1 if premium else 1.0
    total_boost = manager_boost * friend_boost * premium_boost

    total = 0
    report_lines = []
    for count, tier, name in st.session_state.buildings:
        if name in DATA and tier in DATA[name]:
            rate = DATA[name][tier]
            subtotal = count * rate
            total += subtotal
            report_lines.append(f"{count}× {tier} {name}: {subtotal:.2f}/s")
        else:
            report_lines.append(f"⚠️ {name} [{tier}] not found.")

    boosted = total * total_boost

    st.subheader("📊 Results")
    st.markdown("\n".join(report_lines))
    st.markdown(f"**👤 Manager Boost:** x{manager_boost}")
    st.markdown(f"**🤝 Friend Boost:** x{friend_boost:.2f}")
    st.markdown(f"**⭐ Premium Boost:** x{premium_boost:.1f}")
    st.markdown(f"**🔗 Total Multiplier:** x{total_boost:.2f}")
    st.markdown(f"**💰 Base:** {total:.2f}/s")
    st.markdown(f"**💰 Boosted:** {boosted:.2f}/s")
    st.markdown(f"**⏱️ Minute:** {boosted*60:.2f}")
    st.markdown(f"**⏱️ Hour:** {boosted*3600:.2f}")
