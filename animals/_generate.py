"""
個性心理学・12動物 A4横HTML図解ジェネレータ
データソース: personalityChapters.js
"""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

GROUP_INFO = {
    "SUN": {
        "main": "#ea580c", "light": "#ffedd5", "dark": "#9a3412",
        "bg": "linear-gradient(135deg, #fff7ed 0%, #ffffff 60%)",
        "label": "SUN（太陽）", "ratio": "約25%",
        "pillar": "完了", "goal": "成功者",
        "desc": "可能性を大切にし、世の中に広めていく",
        "kuse": "「すごい」「絶対」「面倒くさい」",
        "tokucho": "ムラがある",
        "janken": "パー（外に拡大展開）",
        "icon": "☀️",
    },
    "EARTH": {
        "main": "#059669", "light": "#d1fae5", "dark": "#064e3b",
        "bg": "linear-gradient(135deg, #ecfdf5 0%, #ffffff 60%)",
        "label": "EARTH（地球）", "ratio": "約40%",
        "pillar": "目的", "goal": "財産家",
        "desc": "自分の夢を大切にし、形を作る",
        "kuse": "「一生懸命」「納得」",
        "tokucho": "ムリをする",
        "janken": "チョキ（不要なモノを切り取る）",
        "icon": "🌏",
    },
    "MOON": {
        "main": "#2563eb", "light": "#dbeafe", "dark": "#1e3a8a",
        "bg": "linear-gradient(135deg, #eff6ff 0%, #ffffff 60%)",
        "label": "MOON（月）", "ratio": "約35%",
        "pillar": "調和", "goal": "人格者",
        "desc": "人との関わりを大切にする",
        "kuse": "「なんで〜？」「どうして〜？」",
        "tokucho": "ムダが多い",
        "janken": "グー（小さくまとまる）",
        "icon": "🌙",
    },
}

ALL_STEPS = ["見る", "思いつく", "聞く", "考える", "やる"]

ANIMALS = [
    # ========== SUN ==========
    {
        "name": "ペガサス", "emoji": "🦄", "group": "SUN",
        "tagline": "気分屋さんな天才肌",
        "stage": "胎児（魂）",
        "stage_desc": "最もシンプル・純粋なエネルギー",
        "flow": ["見る", "やる"],
        "strengths": ["発想力に富む", "華がある", "天才肌の閃き", "シンプルな行動力"],
        "weaknesses": ["気分のムラがある", "テンションに波がある", "理屈で動けない"],
        "axes": {"brain": "右脳", "time": "未来展望", "decision": "状況対応"},
        "mistakes": [
            "ミスを忘れるミス",
            "テンションにムラがあってミス",
            "聞く前に行動してミス",
            "気分屋の天才ゆえの落とし穴",
        ],
        "note": "12動物の中で最もシンプルな行動パターン。直感と気分で動く。",
    },
    {
        "name": "チーター", "emoji": "🐆", "group": "SUN",
        "tagline": "取り掛かりがとにかく早い",
        "stage": "中学生",
        "stage_desc": "勢いとスピード重視のエネルギー",
        "flow": ["見る", "聞く", "やる"],
        "strengths": ["ポジティブ思考", "チャレンジ精神", "取り掛かりの早さ", "切り替えが速い"],
        "weaknesses": ["諦めも早い", "持続力が弱い", "カッコつけがち"],
        "axes": {"brain": "左脳", "time": "未来展望", "decision": "状況対応"},
        "mistakes": [
            "ミスを完了してて（忘れて）ミス",
            "早すぎてミス",
            "カッコつけて自信過剰・頑固でミス",
            "走り出したら止まれない性格",
        ],
        "note": "ダッシュ力No.1。短距離ランナータイプ。",
    },
    {
        "name": "ライオン", "emoji": "🦁", "group": "SUN",
        "tagline": "やると決めたら徹底的",
        "stage": "働き盛り",
        "stage_desc": "責任ある立場で力を発揮する年代",
        "flow": ["見る", "聞く", "考える", "やる"],
        "strengths": ["王道を貫く", "ズルや小細工が嫌い", "徹底力", "リーダーシップ"],
        "weaknesses": ["心配性で完璧主義", "他人にも厳しい", "心許せる人の前では猫になる"],
        "axes": {"brain": "左脳", "time": "過去回想", "decision": "状況対応"},
        "mistakes": [
            "心配して完璧を求めすぎてミス",
            "他人にも厳しすぎてミス",
            "何でも事前に知らないと不安な心配屋さん",
        ],
        "note": "百獣の王の風格。裏表のないストレートな性格。",
    },
    {
        "name": "ゾウ", "emoji": "🐘", "group": "SUN",
        "tagline": "強い信念と実行力",
        "stage": "人生の終盤",
        "stage_desc": "経験に裏打ちされた重厚なエネルギー",
        "flow": ["見る", "思いつく", "考える", "聞く", "やる"],
        "strengths": ["やり切る力", "スケールの大きさ", "強い信念", "実行力"],
        "weaknesses": ["人の話が耳に入りにくい", "頑固", "切り替えが遅い"],
        "axes": {"brain": "右脳", "time": "過去回想", "decision": "状況対応"},
        "mistakes": [
            "肝心な話を聞いてなくてミス",
            "自分を棚に上げすぎてミス",
            "人の話や忠告が耳に入りにくい",
        ],
        "note": "一度進み出すと止まらない重戦車型。最も慎重な行動パターン。",
    },
    # ========== EARTH ==========
    {
        "name": "狼", "emoji": "🐺", "group": "EARTH",
        "tagline": "自分の流儀を大事にする",
        "stage": "胎児",
        "stage_desc": "オリジナル・始まりのエネルギー",
        "flow": ["見る", "思いつく", "やる"],
        "strengths": ["マイペース", "独自の世界観", "発想がオリジナル", "周りに流されない"],
        "weaknesses": ["人と同じが嫌いな天邪鬼", "群れるのが苦手", "1人の時間と空間が必須"],
        "axes": {"brain": "右脳", "time": "未来展望", "decision": "目標思考"},
        "mistakes": [
            "思いこみによる根本的なミス",
            "言葉足らずでミス",
            "ミスの概念がないこと自体がミス",
            "前提を飛ばして言葉足らずになりがち",
        ],
        "note": "群れない一匹狼。独自路線を歩む孤高の存在。",
    },
    {
        "name": "猿", "emoji": "🐵", "group": "EARTH",
        "tagline": "褒められるの大好きなお調子者",
        "stage": "小学生",
        "stage_desc": "好奇心旺盛で器用なエネルギー",
        "flow": ["見る", "聞く", "やる"],
        "strengths": ["損得計算が早い", "器用になんでもこなす", "ノリが良い", "切り替え上手"],
        "weaknesses": ["長期戦が苦手", "気力が切れやすい", "目先の損得に弱い"],
        "axes": {"brain": "左脳", "time": "未来展望", "decision": "目標思考"},
        "mistakes": [
            "自分自身のメリットばかり考えてミス",
            "目先の損得だけで決めつけてミス",
            "短期的な損得に引っ張られる",
        ],
        "note": "褒めて伸びるタイプ。瞬発力はあるが持続力が課題。",
    },
    {
        "name": "虎", "emoji": "🐯", "group": "EARTH",
        "tagline": "安定感とバランス感覚のビジネスマン",
        "stage": "部長・社長",
        "stage_desc": "組織を動かす責任感あるエネルギー",
        "flow": ["見る", "聞く", "考える", "やる"],
        "strengths": ["義理人情に厚い", "博愛精神", "バランス感覚", "安定感"],
        "weaknesses": ["臨機応変な対応が苦手", "計画重視で機会を逃す", "悪気なく厳しい一言"],
        "axes": {"brain": "左脳", "time": "過去回想", "decision": "目標思考"},
        "mistakes": [
            "考え整理してる間に期を失うミス",
            "笑顔できついこと言ってミス",
            "マイペースなことがミス",
        ],
        "note": "計画と段取りの達人。組織の中核を担うタイプ。",
    },
    {
        "name": "コアラ", "emoji": "🐨", "group": "EARTH",
        "tagline": "妄想を広げるロマンチスト",
        "stage": "年金",
        "stage_desc": "ゆったりとした熟成のエネルギー",
        "flow": ["見る", "思いつく", "考える", "聞く", "やる"],
        "strengths": ["アイディアと構想力", "長期戦に強い", "ロマンチスト", "妄想力"],
        "weaknesses": ["計算と妄想は進むが実行力に欠ける", "結論を出すまで慎重すぎる", "派閥を作りがち"],
        "axes": {"brain": "右脳", "time": "過去回想", "decision": "目標思考"},
        "mistakes": [
            "思い描いたプランを理解されずにミス",
            "結論を出すために慎重になりすぎてミス",
            "派閥をつくってミス",
        ],
        "note": "構想は壮大、実行はゆっくり。長期プランナータイプ。",
    },
    # ========== MOON ==========
    {
        "name": "こじか", "emoji": "🦌", "group": "MOON",
        "tagline": "友だち作りが大得意な愛されキャラ",
        "stage": "赤ちゃん",
        "stage_desc": "無垢で愛されるエネルギー",
        "flow": ["見る", "思いつく", "やる"],
        "strengths": ["愛情深い", "相手を喜ばせる", "懐の広さ", "純粋さ"],
        "weaknesses": ["駆け引きや計算が苦手", "八方美人になりがち", "ストレスを貯めやすい"],
        "axes": {"brain": "右脳", "time": "未来展望", "decision": "状況対応"},
        "moon_phase": "新月",
        "mistakes": [
            "良い格好を見せようとしてミス",
            "予算の見積もりが甘くてミス",
            "八方美人になってストレスを貯めがち",
        ],
        "note": "新月グループ。可愛がられキャラの代表格。",
    },
    {
        "name": "黒ひょう", "emoji": "🐈\u200d⬛", "group": "MOON",
        "tagline": "グループのリーダー的存在",
        "stage": "反抗期",
        "stage_desc": "鋭く尖ったエネルギー",
        "flow": ["見る", "聞く", "考える", "やる"],
        "strengths": ["情報収集力", "責任感が強い", "美意識が高い", "リーダー気質"],
        "weaknesses": ["好き嫌いが激しい", "プライドが高い", "感情を表に出しがち"],
        "axes": {"brain": "左脳", "time": "未来展望", "decision": "目標思考"},
        "moon_phase": "満月",
        "mistakes": [
            "言いにくいこと言わないでミス",
            "感情を表に出したり感情で判断してミス",
            "自分1人で解決しようとしてミス",
            "繊細な心の持ち主、プライドが邪魔をする",
        ],
        "note": "満月グループ。クールでスタイリッシュなリーダー。",
    },
    {
        "name": "たぬき", "emoji": "🦝", "group": "MOON",
        "tagline": "安心感を与える存在",
        "stage": "会長",
        "stage_desc": "場を和ませる円熟のエネルギー",
        "flow": ["見る", "聞く", "考える", "やる"],
        "strengths": ["全方位外交", "場面に応じて化ける", "安心感", "人当たりの良さ"],
        "weaknesses": ["控えめすぎる印象", "返事だけ良くなりがち", "本心が見えにくい"],
        "axes": {"brain": "左脳", "time": "過去回想", "decision": "状況対応"},
        "moon_phase": "新月",
        "mistakes": [
            "ミスをばかしてミス",
            "返事だけ良くてミス",
            "化けれるが故に誤解を生む",
            "良くも悪くも返事がいい",
        ],
        "note": "新月グループ。場の空気を読む達人。古狸の風格。",
    },
    {
        "name": "ひつじ", "emoji": "🐑", "group": "MOON",
        "tagline": "責任感と面倒見",
        "stage": "棺桶",
        "stage_desc": "全てを受け入れる最終のエネルギー",
        "flow": ["見る", "思いつく", "考える", "聞く", "やる"],
        "strengths": ["気配り上手", "調和を生む", "責任感", "面倒見の良さ"],
        "weaknesses": ["見返りがないとストレス", "本音をもこもこ毛皮で隠す", "意見を言わなすぎる"],
        "axes": {"brain": "右脳", "time": "過去回想", "decision": "目標思考"},
        "moon_phase": "満月",
        "mistakes": [
            "意見を言わなすぎてミス",
            "お節介の見返りを求めてミス",
            "事後報告でミス",
            "自分の本音はもこもこ毛皮で隠す",
        ],
        "note": "満月グループ。財布を2つ持つ（自分用と人付き合い用）。",
    },
]


def render_flow(active_steps, group):
    g = GROUP_INFO[group]
    html = []
    for i, step in enumerate(ALL_STEPS):
        is_active = step in active_steps
        if is_active:
            order = active_steps.index(step) + 1
            html.append(
                f'<div class="step active">'
                f'<div class="step-num">{order}</div>'
                f'<div class="step-label">{step}</div>'
                f'</div>'
            )
        else:
            html.append(
                f'<div class="step inactive">'
                f'<div class="step-num">-</div>'
                f'<div class="step-label">{step}</div>'
                f'</div>'
            )
        if i < len(ALL_STEPS) - 1:
            html.append('<div class="arrow">▸</div>')
    return "".join(html)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>個性心理学：{name}</title>
<style>
  @page {{ size: A4 landscape; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: "Hiragino Sans", "Yu Gothic", "Noto Sans JP", sans-serif;
    color: #1f2937; -webkit-font-smoothing: antialiased;
  }}
  .page {{
    width: 297mm; height: 210mm; padding: 9mm 11mm;
    background: {bg};
    position: relative; overflow: hidden;
  }}
  .page::before {{
    content: ""; position: absolute; top: -40mm; right: -40mm;
    width: 120mm; height: 120mm; border-radius: 50%;
    background: {light}; opacity: 0.5; z-index: 0;
  }}
  .inner {{ position: relative; z-index: 1; height: 100%; display: flex; flex-direction: column; }}

  /* ===== Header ===== */
  .header {{
    display: flex; align-items: center; gap: 8mm;
    border-bottom: 3px solid {main}; padding-bottom: 4mm; margin-bottom: 5mm;
  }}
  .emoji-box {{
    font-size: 48pt; line-height: 1; width: 28mm; height: 28mm;
    display: flex; align-items: center; justify-content: center;
    background: white; border-radius: 50%; border: 3px solid {main};
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    flex-shrink: 0;
  }}
  .title-area {{ flex: 1; }}
  .name {{ font-size: 32pt; font-weight: 900; color: {dark}; line-height: 1; }}
  .tagline {{ font-size: 14pt; color: {main}; margin-top: 2mm; font-weight: 600; }}
  .group-badge {{
    display: inline-flex; align-items: center; gap: 4px;
    padding: 3px 12px; background: {main}; color: white;
    border-radius: 999px; font-size: 11pt; font-weight: 700;
    box-shadow: 0 2px 6px rgba(0,0,0,0.12);
  }}
  .moon-phase {{
    display: inline-block; margin-left: 6px; padding: 2px 8px;
    background: white; color: {dark}; border: 1.5px solid {dark};
    border-radius: 999px; font-size: 9pt; font-weight: 700;
  }}

  /* ===== Main grid ===== */
  .main-grid {{
    display: grid; grid-template-columns: 1.1fr 1.4fr 1fr; gap: 5mm;
    flex: 1; min-height: 0;
  }}
  .col {{ display: flex; flex-direction: column; gap: 4mm; }}

  .card {{
    background: white; border-radius: 8px; padding: 4mm 5mm;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border-top: 3px solid {main};
  }}
  .card h3 {{
    font-size: 10.5pt; color: {dark}; margin-bottom: 2.5mm;
    display: flex; align-items: center; gap: 5px;
    font-weight: 800;
  }}
  .card h3::before {{
    content: ""; display: inline-block; width: 4px; height: 13px;
    background: {main}; border-radius: 2px;
  }}

  /* ===== Stage ===== */
  .stage-box {{
    text-align: center; padding: 3mm;
    background: linear-gradient(135deg, {light} 0%, white 100%);
    border-radius: 6px; border: 1.5px dashed {main};
  }}
  .stage-name {{ font-size: 16pt; font-weight: 900; color: {dark}; }}
  .stage-desc {{ font-size: 8.5pt; color: #6b7280; margin-top: 1mm; }}

  /* ===== Flow ===== */
  .flow {{
    display: flex; align-items: center; gap: 2mm;
    flex-wrap: wrap; justify-content: center;
  }}
  .step {{
    display: flex; flex-direction: column; align-items: center;
    padding: 2.5mm 1mm; min-width: 14mm; border-radius: 6px;
    font-size: 9pt;
  }}
  .step.active {{
    background: {main}; color: white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  }}
  .step.inactive {{
    background: #f3f4f6; color: #9ca3af;
  }}
  .step-num {{
    font-size: 7pt; font-weight: 700; opacity: 0.85;
    margin-bottom: 1mm;
  }}
  .step-label {{ font-size: 9.5pt; font-weight: 700; }}
  .arrow {{ font-size: 11pt; color: {dark}; font-weight: 900; }}

  /* ===== Lists ===== */
  ul {{ list-style: none; }}
  ul li {{
    padding: 1.5mm 0 1.5mm 7mm; position: relative;
    font-size: 9.5pt; line-height: 1.45;
    border-bottom: 1px dotted #e5e7eb;
  }}
  ul li:last-child {{ border-bottom: none; }}
  ul.good li::before {{
    content: "◎"; position: absolute; left: 0;
    color: {main}; font-weight: 900; font-size: 11pt;
  }}
  ul.bad li::before {{
    content: "△"; position: absolute; left: 0;
    color: #f59e0b; font-weight: 900; font-size: 11pt;
  }}
  ul.mistake li {{ padding-left: 8mm; font-size: 9.5pt; }}
  ul.mistake li::before {{
    content: "✗"; position: absolute; left: 0;
    color: #dc2626; font-weight: 900; font-size: 11pt;
  }}

  /* ===== Axes ===== */
  .axes {{ display: flex; flex-direction: column; gap: 2.5mm; }}
  .axis {{
    padding: 2mm 3mm; background: #f9fafb; border-radius: 6px;
  }}
  .axis-title {{
    font-size: 8pt; font-weight: 700; color: #6b7280;
    margin-bottom: 1.5mm;
  }}
  .axis-poles {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 2mm;
  }}
  .pole {{
    text-align: center; padding: 2mm 1mm; border-radius: 5px;
    font-size: 10pt; font-weight: 700;
    background: white; color: #9ca3af; border: 1.5px solid #e5e7eb;
  }}
  .pole.on {{
    background: {main}; color: white; border-color: {main};
    box-shadow: 0 2px 6px rgba(0,0,0,0.12);
  }}

  /* ===== Group info ===== */
  .group-info {{
    background: {dark}; color: white; border-radius: 8px;
    padding: 3mm 5mm; display: flex; gap: 5mm;
    align-items: center;
  }}
  .group-icon {{ font-size: 22pt; }}
  .group-detail {{ flex: 1; font-size: 9pt; line-height: 1.4; }}
  .group-detail strong {{ font-size: 10.5pt; }}

  /* ===== Mistake row ===== */
  .mistake-row {{
    margin-top: 4mm; background: white;
    border-left: 5px solid #dc2626; border-radius: 8px;
    padding: 3.5mm 5mm; box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }}
  .mistake-row h3 {{
    font-size: 10.5pt; color: #991b1b; margin-bottom: 2mm; font-weight: 800;
    display: flex; align-items: center; gap: 6px;
  }}
  .mistake-grid {{
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 0 6mm;
  }}

  /* ===== Note ===== */
  .note {{
    margin-top: 2.5mm; font-size: 9pt; color: #4b5563;
    background: rgba(255,255,255,0.7); padding: 2mm 4mm; border-radius: 6px;
    border-left: 3px solid {main};
  }}

  /* ===== Footer ===== */
  .footer {{
    position: absolute; bottom: 3mm; right: 11mm;
    font-size: 7.5pt; color: #9ca3af; z-index: 2;
  }}
  .pagenum {{
    position: absolute; bottom: 3mm; left: 11mm;
    font-size: 7.5pt; color: #9ca3af; z-index: 2;
  }}

  /* ===== Nav back to index ===== */
  .nav-back {{
    position: fixed; top: 12px; left: 12px; z-index: 100;
    background: white; color: {dark}; text-decoration: none;
    padding: 8px 14px; border-radius: 999px;
    font-size: 13px; font-weight: 700;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    border: 1.5px solid {main};
  }}
  @media print {{ .nav-back {{ display: none; }} }}

  /* ===== Mobile responsive ===== */
  @media screen and (max-width: 900px) {{
    body {{ background: {bg}; padding: 60px 0 20px; }}
    .page {{
      width: 100%; height: auto; min-height: auto;
      padding: 16px; background: transparent;
    }}
    .page::before {{ display: none; }}
    .header {{
      flex-direction: column; align-items: flex-start; gap: 12px;
      padding-bottom: 14px; margin-bottom: 16px;
    }}
    .emoji-box {{
      width: 80px; height: 80px; font-size: 44px;
      align-self: center;
    }}
    .title-area {{ width: 100%; text-align: center; }}
    .name {{ font-size: 28px; }}
    .tagline {{ font-size: 15px; margin-top: 6px; }}
    .group-badge {{
      align-self: center; font-size: 13px; padding: 6px 16px;
    }}
    .main-grid {{
      grid-template-columns: 1fr; gap: 12px;
    }}
    .col {{ gap: 12px; }}
    .card {{ padding: 14px 16px; border-radius: 10px; }}
    .card h3 {{ font-size: 15px; margin-bottom: 10px; }}
    .stage-box {{ padding: 12px; }}
    .stage-name {{ font-size: 22px; }}
    .stage-desc {{ font-size: 12px; }}
    .flow {{ gap: 4px; }}
    .step {{ min-width: 56px; padding: 8px 4px; }}
    .step-label {{ font-size: 13px; }}
    .step-num {{ font-size: 10px; }}
    .arrow {{ font-size: 14px; }}
    ul li {{
      font-size: 13.5px; padding: 6px 0 6px 22px;
    }}
    ul li::before {{ font-size: 14px; }}
    .pole {{ font-size: 13px; padding: 8px 4px; }}
    .axis-title {{ font-size: 11px; margin-bottom: 6px; }}
    .group-info {{ padding: 12px 16px; }}
    .group-icon {{ font-size: 30px; }}
    .group-detail {{ font-size: 12px; }}
    .group-detail strong {{ font-size: 14px; }}
    .mistake-row {{ padding: 14px 16px; margin-top: 14px; }}
    .mistake-row h3 {{ font-size: 15px; }}
    .mistake-grid {{ grid-template-columns: 1fr; gap: 0; }}
    ul.mistake li {{ font-size: 13.5px; padding: 6px 0 6px 24px; }}
    .note {{ font-size: 12.5px; padding: 8px 12px; margin-top: 8px; }}
    .footer, .pagenum {{ display: none; }}
  }}
</style>
</head>
<body>
<a href="index.html" class="nav-back">← 一覧</a>
<div class="page">
  <div class="inner">
    <div class="header">
      <div class="emoji-box">{emoji}</div>
      <div class="title-area">
        <div class="name">{name}{moon_phase_html}</div>
        <div class="tagline">{tagline}</div>
      </div>
      <div class="group-badge">{group_icon} {group_label}</div>
    </div>

    <div class="main-grid">
      <!-- 左：人生ステージ + グループ情報 + 行動パターン -->
      <div class="col">
        <div class="card">
          <h3>人生ステージ</h3>
          <div class="stage-box">
            <div class="stage-name">{stage}</div>
            <div class="stage-desc">{stage_desc}</div>
          </div>
        </div>
        <div class="card">
          <h3>行動パターン</h3>
          <div class="flow">{flow_html}</div>
        </div>
        <div class="group-info">
          <div class="group-icon">{group_icon}</div>
          <div class="group-detail">
            <strong>{group_label}</strong> {group_ratio}<br>
            柱: {group_pillar} ／ 目指す姿: {group_goal}<br>
            {group_desc}
          </div>
        </div>
      </div>

      <!-- 中：強み・弱み -->
      <div class="col">
        <div class="card" style="flex:1;">
          <h3>強み</h3>
          <ul class="good">{strengths_html}</ul>
        </div>
        <div class="card" style="flex:1;">
          <h3>弱み</h3>
          <ul class="bad">{weaknesses_html}</ul>
        </div>
      </div>

      <!-- 右：分類軸 + メモ -->
      <div class="col">
        <div class="card" style="flex:1;">
          <h3>3つの分類軸</h3>
          <div class="axes">
            <div class="axis">
              <div class="axis-title">脳型</div>
              <div class="axis-poles">
                <div class="pole {brain_r}">右脳</div>
                <div class="pole {brain_l}">左脳</div>
              </div>
            </div>
            <div class="axis">
              <div class="axis-title">時間軸</div>
              <div class="axis-poles">
                <div class="pole {time_f}">未来展望</div>
                <div class="pole {time_p}">過去回想</div>
              </div>
            </div>
            <div class="axis">
              <div class="axis-title">意思決定</div>
              <div class="axis-poles">
                <div class="pole {dec_g}">目標思考</div>
                <div class="pole {dec_s}">状況対応</div>
              </div>
            </div>
          </div>
          <div class="note">{note}</div>
        </div>
      </div>
    </div>

    <div class="mistake-row">
      <h3>✗ ミスの傾向</h3>
      <div class="mistake-grid">
        <ul class="mistake">{mistakes_left_html}</ul>
        <ul class="mistake">{mistakes_right_html}</ul>
      </div>
    </div>
  </div>
  <div class="pagenum">個性心理学・12動物図鑑</div>
  <div class="footer">{group_label} / {name}</div>
</div>
</body>
</html>
"""


def render_animal(animal):
    g = GROUP_INFO[animal["group"]]
    flow_html = render_flow(animal["flow"], animal["group"])
    strengths_html = "".join(f"<li>{s}</li>" for s in animal["strengths"])
    weaknesses_html = "".join(f"<li>{w}</li>" for w in animal["weaknesses"])

    mistakes = animal["mistakes"]
    half = (len(mistakes) + 1) // 2
    mistakes_left = mistakes[:half]
    mistakes_right = mistakes[half:]
    mistakes_left_html = "".join(f"<li>{m}</li>" for m in mistakes_left)
    mistakes_right_html = "".join(f"<li>{m}</li>" for m in mistakes_right)

    moon_phase_html = ""
    if "moon_phase" in animal:
        moon_phase_html = f'<span class="moon-phase">{animal["moon_phase"]}</span>'

    axes = animal["axes"]
    on = lambda v: "on" if v else ""

    html = PAGE_TEMPLATE.format(
        name=animal["name"],
        emoji=animal["emoji"],
        tagline=animal["tagline"],
        moon_phase_html=moon_phase_html,
        stage=animal["stage"],
        stage_desc=animal["stage_desc"],
        flow_html=flow_html,
        strengths_html=strengths_html,
        weaknesses_html=weaknesses_html,
        mistakes_left_html=mistakes_left_html,
        mistakes_right_html=mistakes_right_html,
        note=animal["note"],
        brain_r=on(axes["brain"] == "右脳"),
        brain_l=on(axes["brain"] == "左脳"),
        time_f=on(axes["time"] == "未来展望"),
        time_p=on(axes["time"] == "過去回想"),
        dec_g=on(axes["decision"] == "目標思考"),
        dec_s=on(axes["decision"] == "状況対応"),
        main=g["main"], light=g["light"], dark=g["dark"], bg=g["bg"],
        group_label=g["label"], group_ratio=g["ratio"],
        group_pillar=g["pillar"], group_goal=g["goal"],
        group_desc=g["desc"], group_icon=g["icon"],
    )
    return html


INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>個性心理学・12動物図鑑</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: "Hiragino Sans", "Yu Gothic", "Noto Sans JP", sans-serif;
    background: linear-gradient(135deg, #f9fafb 0%, #ffffff 100%);
    color: #1f2937; min-height: 100vh; padding: 32px 16px;
  }}
  .container {{ max-width: 1100px; margin: 0 auto; }}
  h1 {{
    font-size: 28px; font-weight: 900; color: #111827; margin-bottom: 8px;
    text-align: center;
  }}
  .sub {{
    text-align: center; color: #6b7280; margin-bottom: 28px;
    font-size: 13px; line-height: 1.6;
  }}
  .group-section {{ margin-bottom: 28px; }}
  .group-title {{
    display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
    font-size: 16px; font-weight: 800; margin-bottom: 12px;
    padding: 10px 14px; border-radius: 8px; color: white;
  }}
  .group-title.SUN {{ background: linear-gradient(135deg, #ea580c, #f97316); }}
  .group-title.EARTH {{ background: linear-gradient(135deg, #059669, #10b981); }}
  .group-title.MOON {{ background: linear-gradient(135deg, #2563eb, #3b82f6); }}
  .grid {{
    display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 12px;
  }}
  .card {{
    background: white; border-radius: 12px; padding: 18px 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    text-decoration: none; color: inherit;
    transition: transform 0.15s, box-shadow 0.15s;
    display: flex; flex-direction: column; align-items: center;
    text-align: center; border-top: 4px solid var(--c);
  }}
  .card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
  }}
  .card.SUN {{ --c: #ea580c; }}
  .card.EARTH {{ --c: #059669; }}
  .card.MOON {{ --c: #2563eb; }}
  .card-emoji {{ font-size: 40px; margin-bottom: 8px; }}
  .card-name {{ font-size: 16px; font-weight: 800; margin-bottom: 4px; }}
  .card-tagline {{ font-size: 11px; color: #6b7280; line-height: 1.4; }}
  .card-stage {{
    margin-top: 8px; font-size: 10px; color: var(--c); font-weight: 700;
    padding: 2px 8px; background: #f3f4f6; border-radius: 999px;
  }}
  footer {{
    text-align: center; margin-top: 40px; padding: 20px;
    font-size: 12px; color: #9ca3af;
  }}
  @media print {{
    body {{ background: white; padding: 20px; }}
  }}
</style>
</head>
<body>
<div class="container">
  <h1>個性心理学・12動物図鑑</h1>
  <p class="sub">A4横1枚 / 動物別の特性・行動パターン・分類軸・ミスの傾向</p>

  {sections}

  <footer>たまごの相談部屋 / 個性心理学 学習資料</footer>
</div>
</body>
</html>
"""


def render_index():
    groups_order = ["SUN", "EARTH", "MOON"]
    sections = []
    for grp in groups_order:
        gi = GROUP_INFO[grp]
        cards = []
        for a in ANIMALS:
            if a["group"] != grp:
                continue
            cards.append(
                f'<a class="card {grp}" href="animal-{a["name"]}.html">'
                f'<div class="card-emoji">{a["emoji"]}</div>'
                f'<div class="card-name">{a["name"]}</div>'
                f'<div class="card-tagline">{a["tagline"]}</div>'
                f'<div class="card-stage">{a["stage"]}</div>'
                f'</a>'
            )
        sections.append(
            f'<div class="group-section">'
            f'<div class="group-title {grp}">{gi["icon"]} {gi["label"]} '
            f'<span style="font-size:13px;opacity:0.9;">— {gi["pillar"]}を柱に「{gi["goal"]}」を目指す（{gi["ratio"]}）</span>'
            f'</div>'
            f'<div class="grid">{"".join(cards)}</div>'
            f'</div>'
        )
    return INDEX_TEMPLATE.format(sections="\n".join(sections))


def main():
    for animal in ANIMALS:
        html = render_animal(animal)
        path = os.path.join(OUT_DIR, f'animal-{animal["name"]}.html')
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {path}")

    index_html = render_index()
    index_path = os.path.join(OUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"✓ {index_path}")
    print(f"\n計 {len(ANIMALS) + 1} ファイル生成完了")


if __name__ == "__main__":
    main()
