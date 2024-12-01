import streamlit as st
from main import Task_10

def main():
    st.title("DES Algorithm - Task 10")
    st.write("Calculate Ri in DES algorithm round using S-box outputs and Li-1")

    # Add permutation checkbox
    permutation = st.checkbox("Apply permutation to S-box?", value=False)

    # Input method selection
    input_method = st.radio(
        "Choose input method:",
        ["Manual Input", "Random Generation"]
    )

    if input_method == "Manual Input":
        # Manual input fields
        s_box = st.text_input(
            "Enter S-box output (32 bits):",
            value="",
            max_chars=32,
            help="Enter a 32-bit binary string"
        )

        li_1 = st.text_input(
            "Enter Li-1 (32 bits):",
            value="",
            max_chars=32,
            help="Enter a 32-bit binary string"
        )

        # Validation
        if st.button("Calculate Ri"):
            if len(s_box) != 32 or len(li_1) != 32:
                st.error("Both inputs must be exactly 32 bits long!")
            elif not all(bit in '01' for bit in s_box) or not all(bit in '01' for bit in li_1):
                st.error("Inputs must contain only 0s and 1s!")
            else:
                # Create Task_10 instance and run calculation
                task = Task_10(s_box, li_1, permutation)
                result = task.run()

                # Display results
                st.subheader("Results:")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Inputs:")
                    st.code(f"S-box: {s_box}")
                    st.code(f"Li-1:  {li_1}")
                with col2:
                    st.write("Output:")
                    st.code(f"Ri:    {result}")
    else:
        if st.button("Generate Random Values and Calculate"):
            # Generate random values
            s_box = ''.join(str(bit) for bit in Task_10.generate_randomly())
            li_1 = ''.join(str(bit) for bit in Task_10.generate_randomly())

            # Create Task_10 instance and run calculation
            task = Task_10(s_box, li_1, permutation)
            result = task.run()

            # Display results
            st.subheader("Results:")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Inputs:")
                st.code(f"S-box: {s_box}")
                st.code(f"Li-1:  {li_1}")
            with col2:
                st.write("Output:")
                st.code(f"Ri:    {result}")

    # Add explanation
    with st.expander("How it works"):
        st.write("""
        This implementation of DES Task 10:
        1. Takes two 32-bit inputs: S-box outputs and Li-1
        2. Optionally applies permutation to S-box outputs
        3. Performs XOR operation between the inputs
        4. Returns the resulting Ri value

        The calculation follows the DES algorithm's round computation where:
        Ri = Li-1 ⊕ F(Ri-1, Ki)
        """)

if __name__ == "__main__":
    main()