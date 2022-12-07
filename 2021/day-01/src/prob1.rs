use std::{
    error::Error,
    io::{BufRead, Lines},
};

pub fn solve<F>(lines: &mut Lines<F>) -> Result<String, Box<dyn Error>>
where
    F: Sized + BufRead,
{
    let mut count: i16 = 0;
    let mut prev: Option<i16> = None;

    for line in lines {
        let n = i16::from_str_radix(line?.as_str(), 10)?;
        if let Some(p) = prev {
            if n > p {
                count += 1;
            }
        }
        prev = Some(n);
    }

    Ok(format!("{}", count))
}
