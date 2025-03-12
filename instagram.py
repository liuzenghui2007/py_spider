import pandas as pd
import tldextract
import openai
import time
import os

# Configuration
input_file = 'instagram_influencer.csv'
output_file = 'instagram_influencer_ecommerce.csv'
base_url = "https://api.302.ai/v1/chat/completions"
api_key = "sk-1G3R353Ut5L5VQ6vZEGYnaTnw2DoajaOMzgNHrbcJQA5YkdE"
delay = 1

# Set up OpenAI client
client = openai.OpenAI(
    api_key=api_key,
    base_url=base_url
)

def extract_domains(urls):
    """Extract domains from a list of URLs."""
    domains = set()
    for url in urls:
        url = url.strip()
        if not url:
            continue
        
        try:
            ext = tldextract.extract(url)
            if ext.domain and ext.suffix:
                if ext.subdomain and ext.subdomain != 'www':
                    domain = f"{ext.subdomain}.{ext.domain}.{ext.suffix}"
                else:
                    domain = f"{ext.domain}.{ext.suffix}"
                domains.add(domain)
        except Exception as e:
            print(f"Error processing URL: {url}, Error: {e}")
    
    return list(domains)

def is_ecommerce_domain(domains):
    """Determine if domains are e-commerce sites using OpenAI."""
    if not domains:
        return []
    
    prompt = f"""
    Please analyze the following list of domains and identify which ones are e-commerce websites (online shopping, retail, official brand stores, etc.).
    Return only the domains that are confirmed to be e-commerce sites, one per line, with no additional text.
    If there are no e-commerce sites, return "No e-commerce sites".
    
    Domain list:
    {', '.join(domains)}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use the appropriate model
            messages=[
                {"role": "system", "content": "You are an expert in identifying e-commerce websites."},
                {"role": "user", "content": prompt},
            ]
        )
        
        result = response.choices[0].message.content.strip()
        if result == "No e-commerce sites":
            return []
        
        # Split the result into a list
        ecommerce_domains = [domain.strip() for domain in result.split('\n') if domain.strip()]
        return ecommerce_domains
    
    except Exception as e:
        print(f"API call error: {e}")
        return []

def process_csv(input_file, output_file):
    """Process CSV file to extract e-commerce domains."""
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Ensure correct column names
        if 'Username' not in df.columns or 'Bio Links' not in df.columns:
            print("CSV file must contain 'Username' and 'Bio Links' columns")
            return
        
        # Add new column
        df['E-commerce Domains'] = None
        
        # Iterate over each row
        for index, row in df.iterrows():
            username = row['Username']
            bio_links = row['Bio Links']
            
            print(f"Processing user {username} ({index+1}/{len(df)})")
            
            # Skip if Bio Links is empty
            if pd.isna(bio_links) or not bio_links:
                continue
            
            # Split Bio Links
            urls = bio_links.split(',')
            
            # Extract domains
            domains = extract_domains(urls)
            
            # Determine if they are e-commerce sites
            ecommerce_domains = is_ecommerce_domain(domains)
            
            # Update DataFrame
            if ecommerce_domains:
                df.at[index, 'E-commerce Domains'] = '\n'.join(ecommerce_domains)
            
            # Avoid API rate limits
            time.sleep(delay)
        
        # Save results
        df.to_csv(output_file, index=False)
        print(f"Processing complete, results saved to {output_file}")
    
    except Exception as e:
        print(f"Error processing CSV file: {e}")

if __name__ == "__main__":
    process_csv(input_file, output_file)
