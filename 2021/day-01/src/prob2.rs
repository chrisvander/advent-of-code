use std::{
    collections::VecDeque,
    error::Error,
    io::{BufRead, Lines},
};

pub fn solve<F>(lines: &mut Lines<F>) -> Result<String, Box<dyn Error>>
where
    F: Sized + BufRead,
{
    let mut count: i16 = 0;
    let mut prev: Option<i16> = None;
    let mut buf: VecDeque<i16> = VecDeque::with_capacity(3);

    for line in lines {
        let n = i16::from_str_radix(line?.as_str(), 10)?;

        buf.push_back(n);
        if buf.len() < 3 {
            continue;
        } else if buf.len() > 3 {
            buf.pop_front();
        }

        let sm: i16 = buf.iter().sum();
        if let Some(p) = prev {
            if p < sm {
                count += 1
            }
        }

        prev = Some(sm);
    }

    Ok(format!("{}", count))
}
