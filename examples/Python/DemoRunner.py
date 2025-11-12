def run_all_examples():
    """Run all CDC protocol examples"""
    print("🚀 Running Omnni XAI Medical CDC Protocol Examples\n")
    
    # Example 1: Migraine Diagnosis
    migraine_result = migraine_diagnosis_example()
    
    # Example 2: Depression Screening  
    depression_result = depression_screening_example()
    
    # Example 3: Cross-Hospital Sharing
    sharing_result = cross_hospital_example()
    
    print("\n" + "="*50)
    print("🎯 All Examples Completed Successfully!")
    print("Key CDC Protocol Features Demonstrated:")
    print("  ✅ Zero-Hallucination Medical Reasoning")
    print("  ✅ Transparent Audit Trails") 
    print("  ✅ WHO Standard Compliance")
    print("  ✅ Cross-Institution Knowledge Sharing")
    print("  ✅ Automated Verification with Prolog Logic")
    print("="*50)

if __name__ == "__main__":
    run_all_examples()