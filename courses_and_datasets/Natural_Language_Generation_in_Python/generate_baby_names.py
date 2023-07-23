# Function to generate baby names
def generate_baby_names(n):
    
    # Repeat for each name to be generated
    for i in range(0,n):

        # Flag to indicate when to stop generating characters
        stop=False

	# Number of characters generated so far
        counter=1

	# Define a zero vector to contain the output sequence
        output_seq = np.zeros((1, max_len+1, 28))

        # Initialize the first character of output sequence as the start token
        output_seq[0, 0, char_to_idx['\t']] = 1.

	# Variable to contain the name
        name = ''

        # Repeat until the end token is generated or we get the maximum no of characters
        while stop == False and counter < 10:

            # Get probabilities for the next character in sequence
            # probs = model.predict_proba(output_seq, verbose=0)[:,counter-1,:]
            probs = model.predict(output_seq, verbose=0)[:,counter-1,:]

            # Sample the vocabulary according to the probability distribution
            c = np.random.choice(sorted(list(vocabulary)), replace=False, p=probs.reshape(28))
            
            if c=='\n':
                # Stop if end token is encountered, else append to existing sequence
                stop=True
            else:
                # Append this character to the name generated so far
                name = name + c

                # Append this character to existing sequence for prediction of next characters
                output_seq[0,counter , char_to_idx[c]] = 1.
                
                # Increment the number of characters generated
                counter=counter+1

        # Output generated sequence or name
        print(name)