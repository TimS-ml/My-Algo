/*
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)
*/

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 1..prices.len() {
            let gap = prices[i] - prices[i - 1];
            if gap > 0 {
                ans += gap;
            }
        }
        ans
    }
}

// Function to read lines from a file
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() -> io::Result<()> {
    // Path to the test file
    let filename = "122.txt";
    
    // Get an iterator over the lines of the file
    let lines = read_lines(filename)?;
    
    let mut test_case = 1;
    let mut line_iter = lines.map(|l| l.unwrap());
    
    loop {
        // Read number of prices
        let n: usize = match line_iter.next() {
            Some(line) => match line.trim().parse() {
                Ok(num) => num,
                Err(_) => continue, // Skip if not a valid number
            },
            None => break, // End of file
        };
        
        if n == 0 {
            break; // End of file marker
        }
        
        // Read prices
        let prices_line = line_iter.next().unwrap();
        let prices: Vec<i32> = prices_line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        
        // Read expected result
        let expected: i32 = line_iter.next().unwrap().trim().parse().unwrap();
        
        // Compute result
        let result = Solution::max_profit(prices);
        
        // Print result
        println!(
            "Test Case {}: {}, {}",
            test_case,
            result,
            if result == expected { "Correct" } else { "Wrong" }
        );
        
        test_case += 1;
    }
    
    Ok(())
}
