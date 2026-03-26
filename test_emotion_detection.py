from emotion_detection import emotion_detector

def test_emotion_detector():
    # Test case 1: Joy
    result1 = emotion_detector("I am glad this happened")
    assert result1['dominant_emotion'] == 'joy', f"Expected joy, got {result1['dominant_emotion']}"
    
    # Test case 2: Anger
    result2 = emotion_detector("I am really mad about this")
    assert result2['dominant_emotion'] == 'anger', f"Expected anger, got {result2['dominant_emotion']}"
    
    # Test case 3: Disgust
    result3 = emotion_detector("I feel disgusted just hearing about this")
    assert result3['dominant_emotion'] == 'disgust', f"Expected disgust, got {result3['dominant_emotion']}"
    
    # Test case 4: Sadness
    result4 = emotion_detector("I am so sad about this")
    assert result4['dominant_emotion'] == 'sadness', f"Expected sadness, got {result4['dominant_emotion']}"
    
    # Test case 5: Fear
    result5 = emotion_detector("I am really afraid that this will happen")
    assert result5['dominant_emotion'] == 'fear', f"Expected fear, got {result5['dominant_emotion']}"
    
    print("All tests passed successfully!")

if __name__ == "__main__":
    test_emotion_detector()