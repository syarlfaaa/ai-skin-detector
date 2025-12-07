def get_knowledge_page(gradio_url):
    """Skincare knowledge page before redirecting to Gradio"""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Skincare Knowledge - AI Skin Detector</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 40px 20px;
            }}
            
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background: white;
                border-radius: 20px;
                padding: 50px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 40px;
            }}
            
            .header h1 {{
                color: #667eea;
                font-size: 36px;
                margin-bottom: 10px;
            }}
            
            .header p {{
                color: #666;
                font-size: 16px;
            }}
            
            .icon {{
                font-size: 64px;
                margin-bottom: 20px;
            }}
            
            .content {{
                line-height: 1.8;
                color: #444;
            }}
            
            .content h2 {{
                color: #667eea;
                margin: 30px 0 15px 0;
                font-size: 24px;
            }}
            
            .content p {{
                margin-bottom: 15px;
            }}
            
            .skin-types {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }}
            
            .skin-type-card {{
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                padding: 25px;
                border-radius: 15px;
                transition: transform 0.3s;
            }}
            
            .skin-type-card:hover {{
                transform: translateY(-5px);
            }}
            
            .skin-type-card h3 {{
                color: #667eea;
                margin-bottom: 10px;
                font-size: 20px;
            }}
            
            .skin-type-card p {{
                font-size: 14px;
                color: #555;
                margin: 0;
            }}
            
            .tips {{
                background: #f8f9fa;
                padding: 25px;
                border-radius: 15px;
                margin: 30px 0;
                border-left: 5px solid #667eea;
            }}
            
            .tips h3 {{
                color: #667eea;
                margin-bottom: 15px;
            }}
            
            .tips ul {{
                margin-left: 20px;
            }}
            
            .tips li {{
                margin-bottom: 10px;
                color: #555;
            }}
            
            .cta-section {{
                text-align: center;
                margin-top: 50px;
                padding: 40px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px;
                color: white;
            }}
            
            .cta-section h2 {{
                color: white;
                margin-bottom: 15px;
                font-size: 28px;
            }}
            
            .cta-section p {{
                color: rgba(255,255,255,0.9);
                margin-bottom: 25px;
                font-size: 16px;
            }}
            
            .cta-button {{
                display: inline-block;
                padding: 18px 40px;
                background: white;
                color: #667eea;
                text-decoration: none;
                border-radius: 50px;
                font-weight: 600;
                font-size: 18px;
                transition: all 0.3s;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }}
            
            .cta-button:hover {{
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            }}
            
            /* Chatbot Styles */
            .chatbot-container {{
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 380px;
                height: 550px;
                background: white;
                border-radius: 20px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.3);
                display: none;
                flex-direction: column;
                z-index: 1000;
                animation: slideUp 0.3s ease;
            }}
            
            .chatbot-container.open {{
                display: flex;
            }}
            
            @keyframes slideUp {{
                from {{ 
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{ 
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            .chatbot-header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                border-radius: 20px 20px 0 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            
            .chatbot-header h3 {{
                margin: 0;
                font-size: 18px;
            }}
            
            .chatbot-header .close-btn {{
                background: none;
                border: none;
                color: white;
                font-size: 24px;
                cursor: pointer;
                padding: 0;
                width: 30px;
                height: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            
            .chatbot-messages {{
                flex: 1;
                overflow-y: auto;
                padding: 20px;
                background: #f8f9fa;
            }}
            
            .message {{
                margin-bottom: 15px;
                display: flex;
                gap: 10px;
            }}
            
            .message.user {{
                flex-direction: row-reverse;
            }}
            
            .message-content {{
                max-width: 70%;
                padding: 12px 16px;
                border-radius: 15px;
                line-height: 1.4;
                font-size: 14px;
                white-space: pre-wrap;
            }}
            
            .message.bot .message-content {{
                background: white;
                color: #333;
                border: 1px solid #e0e0e0;
            }}
            
            .message.user .message-content {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}
            
            .message-avatar {{
                width: 35px;
                height: 35px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 18px;
                flex-shrink: 0;
            }}
            
            .message.bot .message-avatar {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }}
            
            .message.user .message-avatar {{
                background: #e0e0e0;
            }}
            
            .typing-indicator {{
                display: none;
                padding: 12px 16px;
                background: white;
                border-radius: 15px;
                width: fit-content;
                border: 1px solid #e0e0e0;
            }}
            
            .typing-indicator.show {{
                display: block;
            }}
            
            .typing-indicator span {{
                height: 8px;
                width: 8px;
                background: #667eea;
                border-radius: 50%;
                display: inline-block;
                margin: 0 2px;
                animation: typing 1.4s infinite;
            }}
            
            .typing-indicator span:nth-child(2) {{
                animation-delay: 0.2s;
            }}
            
            .typing-indicator span:nth-child(3) {{
                animation-delay: 0.4s;
            }}
            
            @keyframes typing {{
                0%, 60%, 100% {{
                    transform: translateY(0);
                }}
                30% {{
                    transform: translateY(-10px);
                }}
            }}
            
            .chatbot-input {{
                padding: 20px;
                border-top: 1px solid #e0e0e0;
                display: flex;
                gap: 10px;
            }}
            
            .chatbot-input input {{
                flex: 1;
                padding: 12px 15px;
                border: 2px solid #e0e0e0;
                border-radius: 25px;
                font-size: 14px;
                outline: none;
            }}
            
            .chatbot-input input:focus {{
                border-color: #667eea;
            }}
            
            .chatbot-input button {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: 600;
                transition: all 0.3s;
            }}
            
            .chatbot-input button:hover {{
                transform: scale(1.05);
            }}
            
            .chatbot-toggle {{
                position: fixed;
                bottom: 30px;
                right: 30px;
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
                transition: all 0.3s;
                z-index: 999;
                border: none;
                font-size: 28px;
            }}
            
            .chatbot-toggle:hover {{
                transform: scale(1.1);
                box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
            }}
            
            .chatbot-toggle.hidden {{
                display: none;
            }}
            
            @media (max-width: 768px) {{
                .chatbot-container {{
                    width: calc(100% - 40px);
                    height: calc(100% - 100px);
                    bottom: 20px;
                    right: 20px;
                }}
                
                .chatbot-toggle {{
                    bottom: 20px;
                    right: 20px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="icon">✨</div>
                <h1>Knowledge About Skincare</h1>
                <p>Understanding your skin is the first step to healthy, glowing skin</p>
            </div>
            
            <div class="content">
                <h2>What is Skin Type?</h2>
                <p>
                    Your skin type is determined by how much oil your skin produces. Understanding your skin type 
                    is essential for choosing the right skincare products and routine. There are generally five main skin types.
                </p>
                
                <div class="skin-types">
                    <div class="skin-type-card">
                        <h3>🌟 Normal Skin</h3>
                        <p>Well-balanced, not too oily or dry. Small pores, few imperfections, and a radiant complexion.</p>
                    </div>
                    
                    <div class="skin-type-card">
                        <h3>💧 Dry Skin</h3>
                        <p>Produces less sebum, feels tight and rough. May show more visible lines and lack elasticity.</p>
                    </div>
                    
                    <div class="skin-type-card">
                        <h3>✨ Oily Skin</h3>
                        <p>Produces excess sebum, resulting in a shiny appearance. Enlarged pores and prone to acne.</p>
                    </div>
                    
                    <div class="skin-type-card">
                        <h3>🔄 Combination Skin</h3>
                        <p>Mix of skin types. Usually oily in T-zone (forehead, nose, chin) and normal to dry in other areas.</p>
                    </div>
                    
                    <div class="skin-type-card">
                        <h3>🌺 Sensitive Skin</h3>
                        <p>Easily irritated, prone to redness, itching, and burning. Reacts to certain ingredients or weather.</p>
                    </div>
                </div>
                
                <h2>Why Knowing Your Skin Type Matters</h2>
                <p>
                    Using the wrong products for your skin type can lead to breakouts, irritation, premature aging, 
                    and other skin problems. When you know your skin type, you can:
                </p>
                
                <div class="tips">
                    <h3>💡 Benefits of Knowing Your Skin Type:</h3>
                    <ul>
                        <li><strong>Choose the right products</strong> that work with your skin, not against it</li>
                        <li><strong>Prevent common problems</strong> like acne, dryness, or excessive oiliness</li>
                        <li><strong>Save money</strong> by avoiding products that won't work for you</li>
                        <li><strong>Achieve better results</strong> from your skincare routine</li>
                        <li><strong>Maintain healthy skin</strong> in the long term</li>
                    </ul>
                </div>
                
                <h2>🤖 How Our AI Technology Works</h2>
                <p>
                    Our AI-powered skin detector uses cutting-edge deep learning algorithms trained on thousands 
                    of skin images to provide accurate analysis in seconds. Simply upload a photo, and our AI will:
                </p>
                <div class="tips">
                    <ul>
                        <li>Analyze your skin texture, tone, and condition</li>
                        <li>Identify your exact skin type</li>
                        <li>Detect potential skin concerns</li>
                        <li>Provide personalized product recommendations</li>
                        <li>Suggest a customized skincare routine</li>
                    </ul>
                </div>
            </div>
            
            <div class="cta-section">
                <h2>Ready to Discover Your Skin Type?</h2>
                <p>Let our AI analyze your skin and get personalized skincare recommendations!</p>
                <a href="{gradio_url}" class="cta-button">Check Your Skin Condition Now →</a>
            </div>
        </div>
        
        <!-- Chatbot Toggle Button -->
        <button class="chatbot-toggle" onclick="toggleChatbot()">💬</button>
        
        <!-- Chatbot Container -->
        <div class="chatbot-container" id="chatbot">
            <div class="chatbot-header">
                <h3>🤖 AI Skincare Assistant</h3>
                <button class="close-btn" onclick="toggleChatbot()">×</button>
            </div>
            
            <div class="chatbot-messages" id="chatMessages">
                <div class="message bot">
                    <div class="message-avatar">🤖</div>
                    <div class="message-content">Hi! I'm your AI Skincare Assistant! 👋

I can help you with:
• Skincare advice & tips
• Product recommendations
• Skin concerns & solutions
• General skincare questions

What would you like to know?</div>
                </div>
                <div class="typing-indicator" id="typingIndicator">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            
            <div class="chatbot-input">
                <input 
                    type="text" 
                    id="userInput" 
                    placeholder="Ask me anything about skincare..."
                    onkeypress="handleKeyPress(event)"
                >
                <button onclick="sendMessage()">Send</button>
            </div>
        </div>
        
        <script>
            function toggleChatbot() {{
                const chatbot = document.getElementById('chatbot');
                const toggle = document.querySelector('.chatbot-toggle');
                
                if (chatbot.classList.contains('open')) {{
                    chatbot.classList.remove('open');
                    toggle.classList.remove('hidden');
                }} else {{
                    chatbot.classList.add('open');
                    toggle.classList.add('hidden');
                }}
            }}
            
            function handleKeyPress(event) {{
                if (event.key === 'Enter') {{
                    sendMessage();
                }}
            }}
            
            function sendMessage() {{
                const input = document.getElementById('userInput');
                const message = input.value.trim().toLowerCase();
                
                if (!message) return;
                
                // Add user message
                addMessage(input.value.trim(), 'user');
                input.value = '';
                
                // Show typing indicator
                showTyping(true);
                
                // Simulate AI thinking
                setTimeout(() => {{
                    showTyping(false);
                    const response = getResponse(message);
                    addMessage(response, 'bot');
                }}, 1000 + Math.random() * 1000);
            }}
            
            function getResponse(message) {{
                // Skincare knowledge base
                const responses = {{
                    // Skin Types
                    'oily': "For oily skin, I recommend using oil-free, non-comedogenic products. Look for ingredients like salicylic acid, niacinamide, and clay masks to control excess oil. Make sure to cleanse twice daily but avoid over-washing, which can trigger more oil production!",
                    
                    'dry': "Dry skin needs extra hydration! Use gentle, creamy cleansers and rich moisturizers with hyaluronic acid, ceramides, and glycerin. Don't forget to apply moisturizer while your skin is still damp to lock in hydration. A humidifier at night can also help!",
                    
                    'sensitive': "For sensitive skin, stick to fragrance-free, hypoallergenic products with minimal ingredients. Look for soothing ingredients like centella asiatica, aloe vera, and colloidal oatmeal. Always patch test new products before applying to your entire face!",
                    
                    'combination': "Combination skin can be tricky! Use lightweight, balancing products. You might need to treat different areas differently - use oil-control products on your T-zone and hydrating products on dry areas. A gel-based moisturizer works great for this skin type!",
                    
                    'normal': "Lucky you! Normal skin is well-balanced, but still needs care. Maintain it with a gentle cleanser, moisturizer with SPF during the day, and a good night cream. Focus on prevention and protection to keep your skin healthy!",
                    
                    // Concerns
                    'acne': "For acne, look for products with salicylic acid, benzoyl peroxide, or retinoids. Keep your skin clean but don't over-wash. Avoid touching your face and change your pillowcase regularly. If acne persists or is severe, consider seeing a dermatologist for personalized treatment!",
                    
                    'wrinkle': "To address wrinkles and aging, use products with retinol, vitamin C, and peptides. Always wear SPF 30+ daily - sun damage is the #1 cause of premature aging! Keep skin hydrated and consider adding an antioxidant serum to your routine.",
                    
                    'dark spot': "Dark spots can be treated with vitamin C, niacinamide, alpha arbutin, or kojic acid. Always use SPF to prevent them from getting darker! Results take time - be patient and consistent. For stubborn spots, a dermatologist can offer stronger treatments.",
                    
                    'pore': "To minimize pores, keep them clean with regular cleansing and exfoliation. Use products with niacinamide or retinol. Clay masks once or twice a week can help. Remember, you can't shrink pores permanently, but you can make them appear smaller!",
                    
                    // Routines
                    'routine': "A basic routine includes: Morning - gentle cleanser, toner (optional), serum, moisturizer, and SPF. Night - cleanser, toner (optional), treatment products (like retinol), and night cream. Start simple and add products gradually!",
                    
                    'morning': "Morning routine: 1) Gentle cleanser 2) Vitamin C serum 3) Moisturizer 4) SPF 30+ sunscreen. Keep it simple but effective. The most important step is sunscreen - never skip it!",
                    
                    'night': "Night routine: 1) Oil or balm cleanser (if wearing makeup) 2) Water-based cleanser 3) Toner (optional) 4) Treatment serum (retinol, AHA/BHA) 5) Eye cream 6) Night moisturizer. This is when your skin repairs itself, so nourish it well!",
                    
                    // Products
                    'cleanser': "Choose a cleanser based on your skin type. Oily skin: foaming or gel cleanser. Dry skin: cream or oil cleanser. Sensitive: gentle, fragrance-free formula. Never use harsh soaps on your face! Your skin should feel clean but not tight after cleansing.",
                    
                    'moisturizer': "Everyone needs moisturizer, even oily skin! Choose based on your skin type: gel for oily, cream for dry, lotion for combination. Look for ingredients like hyaluronic acid, ceramides, and glycerin. Apply to damp skin for best absorption!",
                    
                    'sunscreen': "Sunscreen is THE most important skincare product! Use SPF 30+ every day, even indoors and on cloudy days. Reapply every 2 hours if outdoors. Choose mineral (zinc oxide) for sensitive skin or chemical sunscreens for no white cast. This prevents aging and skin cancer!",
                    
                    'serum': "Serums are concentrated treatments. Popular ones include: Vitamin C (brightening, antioxidant), Hyaluronic Acid (hydration), Niacinamide (pores, texture), and Retinol (anti-aging). Apply after cleansing, before moisturizer. Start with one and add more as needed!",
                    
                    // Ingredients
                    'retinol': "Retinol is amazing for anti-aging, acne, and texture! Start slowly (2-3x per week) and always use at night. Your skin may purge or get sensitive initially - this is normal. Always use SPF during the day. Results appear after 8-12 weeks of consistent use!",
                    
                    'vitamin c': "Vitamin C brightens, evens skin tone, and protects against environmental damage. Use in the morning before sunscreen for extra protection. Store in a cool, dark place as it oxidizes easily. Look for L-ascorbic acid for best results!",
                    
                    'hyaluronic acid': "Hyaluronic acid is a hydration superstar! It holds 1000x its weight in water. Apply to damp skin, then seal with moisturizer. It works for all skin types. Use morning and night for plump, hydrated skin!",
                    
                    'niacinamide': "Niacinamide (Vitamin B3) is gentle but effective! It minimizes pores, controls oil, evens tone, and strengthens skin barrier. Works well with most ingredients and suits all skin types. You'll see results in 4-6 weeks!",
                    
                    // General
                    'help': "I can help you with skincare advice, product recommendations, routine building, and answering questions about ingredients! Ask me about skin types, concerns like acne or wrinkles, or specific products you're curious about.",
                    
                    'start': "Starting a skincare routine? Begin with these basics: 1) Gentle cleanser 2) Moisturizer 3) SPF for daytime. Use these for 2-4 weeks, then gradually add treatments based on your concerns. Consistency is key!",
                    
                    'recommend': "I'd love to recommend products! First, tell me: What's your skin type (oily, dry, combination, sensitive)? What are your main concerns (acne, aging, dark spots)? What's your budget? This helps me give you the best suggestions!"
                }};
                
                // Match keywords
                for (const [keyword, response] of Object.entries(responses)) {{
                    if (message.includes(keyword)) {{
                        return response;
                    }}
                }}
                
                // Default responses
                const defaults = [
                    "That's a great question! For specific skin concerns, I recommend consulting with a dermatologist. In the meantime, what's your skin type? I can give you some general tips!",
                    "I'd love to help! Can you tell me more about your skin type or concern? For example: oily skin, acne, wrinkles, or dark spots?",
                    "Interesting question! While I can provide general skincare advice, for personalized recommendations, try our AI Skin Detector! It'll analyze your skin and give specific suggestions. Meanwhile, what would you like to know about skincare?"
                ];
                
                return defaults[Math.floor(Math.random() * defaults.length)];
            }}
            
            function addMessage(text, sender) {{
                const messagesDiv = document.getElementById('chatMessages');
                const messageDiv = document.createElement('div');
                messageDiv.className = `message ${{sender}}`;
                
                const avatar = document.createElement('div');
                avatar.className = 'message-avatar';
                avatar.textContent = sender === 'bot' ? '🤖' : '👤';
                
                const content = document.createElement('div');
                content.className = 'message-content';
                content.textContent = text;
                
                messageDiv.appendChild(avatar);
                messageDiv.appendChild(content);
                messagesDiv.insertBefore(messageDiv, document.getElementById('typingIndicator'));
                
                // Scroll to bottom
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }}
            
            function showTyping(show) {{
                const typing = document.getElementById('typingIndicator');
                if (show) {{
                    typing.classList.add('show');
                }} else {{
                    typing.classList.remove('show');
                }}
                
                // Scroll to bottom
                const messagesDiv = document.getElementById('chatMessages');
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }}
        </script>
    </body>
    </html>
    """